import tornado.web


class AdmissionsHandler(tornado.web.RequestHandler):
    """
    Basic hello world implementation of a Admissions handler class
    """
    def get(self):
        self.render("admissions.html", title="[RMS] Admissions")
