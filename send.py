
class MyHandler(webapp2.RequestHandler):
    def post(self):
        nombre = self.request.get('email_destino')
        
        print nombre