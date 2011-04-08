# Copyright (c) 2007-2009 The PyAMF Project.
# See LICENSE for details.
  """
  Authentication example server.
  
  @see: U{Authentication Howto<http://pyamf.org/wiki/AuthenticationHowto>}
       wiki page.
 
  @since: 0.1.0
  """
  
from wsgiref import simple_server

from pyamf.remoting.gateway.wsgi import WSGIGateway
   
class CalcService:
    def sum(self, a, b):
        return a + b
  
def auth(username, password):
    if username == 'jane' and password == 'doe':
        return True
        
    return False

httpd = simple_server.WSGIServer(('localhost', 8000), simple_server.WSGIRequestHandler)

gateway = WSGIGateway({'calc': CalcService}, authenticator=auth)

httpd.set_app(gateway)

print "Running Authentication AMF gateway on http://localhost:8000"

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
    