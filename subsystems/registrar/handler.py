from tornado import web, template
import os

template_loader = template.Loader(os.path.join(os.path.dirname(__file__), "templates"))


class RegistrarHandler(web.RequestHandler):
    """
    Basic hello world implementation of a Registrar handler class
    """
    def get(self):
        result = template_loader.load("registrar.html").generate(title="[RMS] Registrar")
        self.write(result)
