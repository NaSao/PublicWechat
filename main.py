import webapp2


class MainPage(webapp2.RequestHandler):
    allowed_app_ids = [
        'other-app-id',
        'other-app-id-2'
    ]

    def get(self):
        incoming_app_id = self.request.headers.get(
            'X-Appengine-Inbound-Appid', None)

        if incoming_app_id not in self.allowed_app_ids:
            self.abort(403)

        self.response.write('This is a protected page.')


app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)