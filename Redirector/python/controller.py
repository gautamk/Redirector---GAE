#!/usr/bin/env python
import webapp2
from model import RedirectRoutes




class RedirectHandler(webapp2.RequestHandler):
    def get(self,target_key):
        import logging
        r = RedirectRoutes.get_by_key_name(target_key)
        if r:
            logging.info("Redirected to :"+str(r.target_url)+"\n"+str(self.request.headers))
            self.redirect(str(r.target_url))
        else:
            self.error(404);

class DeleteHandler(webapp2.RequestHandler):
    def post(self):
        key = self.request.get('key')
        RedirectRoutes.get(key).delete()
        self.redirect ('/')
