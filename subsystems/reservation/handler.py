from tornado import web, template
import os

template_loader = template.Loader(os.path.join(os.path.dirname(__file__), "templates"))


class ReservationsHandler(web.RequestHandler):
    """
    Basic hello world implementation of a Reservation handler class
    """
    def get(self):
        result = template_loader.load("reservations.html").generate(title="[RMS] Reservations")
        self.write(result)
