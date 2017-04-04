import tornado.web


class ReservationsHandler(tornado.web.RequestHandler):
    """
    Basic hello world implementation of a Reservation handler class
    """
    def get(self):
        self.render("reservations.html", title="[RMS] Reservations")
