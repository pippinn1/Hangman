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

from datetime import datetime
import webapp2
import os

from google.appengine.ext import ndb
from google.appengine.ext.webapp import template

import models

class BaseHandler(webapp2.RequestHandler):

    def render_template(self, template_name, values):
        path = os.path.join(os.path.dirname(__file__), "static", "html", template_name)
        return template.render(path, values)

class MainHandler(BaseHandler):

    def get(self):

        self.response.write(self.render_template("index.html", {}))

    def post(self):

        question = "Cat"
        question_tokens = question.split()

        # ["C", "a", "t"]

        user_entered_letter = self.request.get("letter")

        # Figure out how to search if user_entered_letter exists in question_tokens

 


        blog_content = self.request.get("letter")
        blog_post = models.BlogPost()
        blog_post.content = blog_content
        blog_post.date = datetime.now()
        blog_post.put()



app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
