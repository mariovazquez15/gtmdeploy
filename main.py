#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.api import images
from google.appengine.api import mail
class MainHandler(webapp.RequestHandler):
    def get(self):
        html = open("templates/index.html",'r').read()
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(html)

    def post(self):
        email_destino = self.request.get("email_destino")
        
        pantallazos = self.request.POST.getall('pantallazos[]')
        entorno = self.request.get("optradio")
        changes = self.request.get("changes")
        email_origen = self.request.get("email_origen")
        datetime = self.request.get("datetime_picker")
        self.response.write("Email destino: " + email_destino + " Changes= " + changes + " Email origen= " + email_origen)
        self.response.write(pantallazos)
        images = []
            
        
        if len(pantallazos) > 0:
            for image in pantallazos:
                images.append((image.filename,image.value))        
                        
            mail.send_mail(sender=email_origen,
                       to=email_destino,
                       subject="Publicacion en " + str(entorno),
                       body="A continuacion puede observar los pantallazos de la subida en " + str(entorno) +".\n\nLos cambios realizados son: \n" +changes+" \n\n Fecha y hora de la subida: " + datetime,
                      attachments=images)
        
        self.response.write("Mail enviado!")
        
    

        
            
        
app = webapp.WSGIApplication([
    ('/', MainHandler)
], debug=True)