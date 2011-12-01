from google.appengine.ext import db

class UniqueConstraintViolation(Exception):
  def __init__(self, scope, value):
    super(UniqueConstraintViolation, self).__init__("Value '%s' is not unique within scope '%s'." % (value, scope, ))

class RedirectRoutes(db.Model):
    author = db.UserProperty(auto_current_user_add = True , required = False)
    target_url = db.LinkProperty(required = True)
    added_at = db.DateTimeProperty(auto_now_add = True)
    modified_at = db.DateTimeProperty(auto_now = True)

    @classmethod
    def hash(target_key):
        from zlib import adler32
        return adler32(target_key)

    @classmethod
    def create(cls,target_key, target_url):
        if(target_key == ""):
            target_key = str(hash(target_url))
        ue = RedirectRoutes.get_by_key_name (target_key)

        if ue:
            raise UniqueConstraintViolation(target_key , target_url)

        r = RedirectRoutes(target_url = target_url , key_name = target_key)
        r.put()
        return r
