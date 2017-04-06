import signal
import os

import tornado.ioloop
import tornado.web
import tornado.template
import tornado.websocket
from subsystems.admissions.handler import AdmissionsHandler
from subsystems.courses.handler import CoursesHandler
from subsystems.financial_aid.handler import FinancialAidHandler
from subsystems.reservation.handler import ReservationsHandler
from subsystems.registrar.handler import RegistrarHandler

# Global variable used to figure out if we are exiting the app or not
is_closing = False

template_loader = tornado.template.Loader(os.path.join(os.path.dirname(__file__), "templates"))


def signal_handler(signum, frame):
    """
    Handle signals like CTRL C and exit properly
    """
    global is_closing
    print('Exiting ...')
    is_closing = True


def try_exit():
    """
    Attempt to exit the tornado app if a singal is caught
    """
    global is_closing
    if is_closing:
        tornado.ioloop.IOLoop.instance().stop()
        print('Exit success')


class HeartBeatReceiver(tornado.websocket.WebSocketHandler):
    """
    Basic heart beat handler to receive messages from open pages
    """
    def open(self):
        print("Opening heartbeat connection")

    def on_message(self, message):
        print(message)

    def on_close(self):
        print("Closing heartbeat connection")

    def check_origin(self, origin):
        return True


class MainHandler(tornado.web.RequestHandler):
    """
    Basic hello world implementation of a main handler class
    """
    def get(self):
        result = template_loader.load("home.html").generate(title="[RMS] Home")
        self.write(result)


def make_app():
    """
    Create the main app, run based on an empty URL
    :return: The tornado webapplication
    """
    template_path = os.path.join(os.path.dirname(__file__), "templates")

    static_path = 'static/'
    return tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/financial-aid/", FinancialAidHandler),
            (r"/courses/", CoursesHandler),
            (r"/admissions/", AdmissionsHandler),
            (r"/registrar/", RegistrarHandler),
            (r"/reservations/", ReservationsHandler),
            (r"/heartbeat", HeartBeatReceiver),
            (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': static_path})
        ],
        template_path=template_path,
    )

# Run the things!
if __name__ == "__main__":
    app = make_app()
    signal.signal(signal.SIGINT, signal_handler)
    app.listen(8888)

    # Register the function to exit tornado, how wonderful that
    # this isn't built in
    tornado.ioloop.PeriodicCallback(try_exit, 100).start()

    print('Starting web server on http://127.0.0.1:8888/ ...')
    tornado.ioloop.IOLoop.instance().start()
