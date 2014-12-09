from google.appengine.ext import ndb

class BlogPost(ndb.Model):

    content = ndb.StringProperty()
    date = ndb.DateTimeProperty()
