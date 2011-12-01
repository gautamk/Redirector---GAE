import os
import webapp2
from model import RedirectRoutes , UniqueConstraintViolation
from google.appengine.ext.webapp import template



class IndexHandler(webapp2.RequestHandler):
    def delete(self):
        print self.request.get('key')

    def post(self):
        
        try:
            RedirectRoutes.create(
            target_key = self.request.get('target_key'),
            target_url = self.request.get('target_url'),
                )
            self.redirect('/')
        except UniqueConstraintViolation:
            self.response.out.write("The target Key already exists , Please go back and try a different key")


    def get(self):
        from google.appengine.api import users
        template_values={
            'self':self,
            'current_user':users.get_current_user(),
            'logout_url':users.create_logout_url(self.request.uri),
            'redirectors':RedirectRoutes.all().filter('author =', users.get_current_user() ),
        }
        path = os.path.join(os.path.dirname(__file__), 'templates/index.html')
        self.response.out.write(template.render(path , template_values))
