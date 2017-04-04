import tornado.web


class CoursesHandler(tornado.web.RequestHandler):
    """
    Basic hello world implementation of a FA handler class
    """
    def get(self):
        self.render("courses.html", title="[RMS] Courses")
