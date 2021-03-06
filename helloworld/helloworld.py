import cgi
import os

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

# Model Class
class Greeting(db.Model):
    author  = db.UserProperty()
    content = db.StringProperty(multiline=True)
    date    = db.DateTimeProperty(auto_now_add=True)

class Secure(webapp.RequestHandler):
    def get(self):
        if users.get_current_user():
            user=users.get_current_user()    
        else:
            self.redirect('/')
        
        template_values = {                           
            'user': user,      
            }
             
        path = os.path.join(os.path.dirname(__file__), 'secure.html')
        self.response.out.write(template.render(path, template_values))
    
        
class MainPage(webapp.RequestHandler):
  def get(self):
    greetings_query = Greeting.all().order('-date')
    greetings = greetings_query.fetch(10)

    if users.get_current_user():
        url = users.create_logout_url(self.request.uri)
        url_linktext = 'Logout'
        username = users.get_current_user().nickname()
    else:
        url = users.create_login_url(self.request.uri)
        url_linktext = 'Login'
        username = "Anonymous"

    template_values = {
      'greetings': greetings,
      'url': url,
      'url_linktext': url_linktext,
      'username': username
      }

    path = os.path.join(os.path.dirname(__file__), 'index.html')
    self.response.out.write(template.render(path, template_values))

class MyGuestbook(webapp.RequestHandler):
  def post(self):
    greeting = Greeting()
    
    if users.get_current_user():
        greeting.author = users.get_current_user()
    
    greeting.content = self.request.get('content')
    greeting.put()
    self.redirect('/')

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/sign', MyGuestbook),
                                      ('/secure', Secure),
                                      ],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()