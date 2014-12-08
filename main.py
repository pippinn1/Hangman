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
import datetime
import webapp2
import os

from google.appengine.ext import ndb
from google.appengine.ext.webapp import template


class BlogPost(ndb.Model):
    date = ndb.DateTimeProperty()
    content = ndb.StringProperty()

class BaseHandler(webapp2.RequestHandler):

    def render_template(self, template_name, values):
        path = os.path.join(os.path.dirname(__file__), "static", "html", template_name)
        return template.render(path, values)

class SecondHandler(webapp2.RequestHandler):

    def get(self):

        self.response.write('Another place on the web!')

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
