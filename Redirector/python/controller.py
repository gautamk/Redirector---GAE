#!/usr/bin/env python
import webapp2
from zlib import adler32
from google.appengine.ext.webapp import util


class IndexHandler(webapp2.RequestHandler):
    def get(self):
        

