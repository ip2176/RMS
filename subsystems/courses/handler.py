from tornado import web, template
import os

template_loader = template.Loader(os.path.join(os.path.dirname(__file__), "templates"))


class CoursesHandler(web.RequestHandler):
    """
    Basic hello world implementation of a Courses handler class
    """
    def get(self):
        result = template_loader.load("courses.html").generate(title="[RMS] Courses")
        self.write(result)
