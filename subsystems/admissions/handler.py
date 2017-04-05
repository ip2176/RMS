from tornado import web, template
import os

template_loader = template.Loader(os.path.join(os.path.dirname(__file__), "templates"))


class AdmissionsHandler(web.RequestHandler):
    """
    Basic hello world implementation of a Admissions handler class
    """
    def get(self):
        result = template_loader.load("admissions.html").generate(title="[RMS] Admissions")
        self.write(result)
