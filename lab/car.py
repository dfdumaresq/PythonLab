import sys #import sys module for printing to stdout
from google.appengine.ext import db

class Car(db.Model):
   brand  =  db.StringProperty(required=True)
   wheels =  db.ListProperty(db.Key)

class Human(db.Model):
    name    = db.StringProperty(required=True)
    drives  = db.ReferenceProperty(reference_class=Car)
    spouse  = db.SelfReferenceProperty()
    owns    = db.ListProperty(db.Key)

class Wheel(db.Model):
    isBroken =  db.BooleanProperty(default=False)
    position =  db.StringProperty(choices=set(["left_front",
                                              "left_back",
                                              "right_front",
                                              "right_back"]))
# one-to-one
jack        = Human(name="Jack")
mercedes    = Car(brand="Mercedes")
jack.drives = mercedes.put()
jack.put()
print >> sys.stdout, "Jack drives a "+jack.drives.brand