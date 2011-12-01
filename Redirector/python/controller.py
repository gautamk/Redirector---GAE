#!/usr/bin/env python
import webapp2
from model import RedirectRoutes




class RedirectHandler(webapp2.RequestHandler):
    def get(self,target_key):
        r = RedirectRoutes.get_by_key_name(target_key)
        if r:
            self.redirect(str(r.target_url))
        else:
            self.error(404)
