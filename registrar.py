import tornado.web


class RegistrarHandler(tornado.web.RequestHandler):
    """
    Basic hello world implementation of a Registrar handler class
    """
    def get(self):
        self.render("registrar.html", title="[RMS] Registrar")
