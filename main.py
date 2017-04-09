import signal
import os
import random

import tornado.ioloop
import tornado.web
import tornado.template
import tornado.websocket
import tornado.httpserver
from subsystems.admissions.handler import AdmissionsHandler
from subsystems.courses.handler import CoursesHandler
from subsystems.financial_aid.handler import FinancialAidHandler
from subsystems.reservation.handler import ReservationsHandler
from subsystems.registrar.handler import RegistrarHandler

# Global variable used to figure out if we are exiting the app or not
is_closing = False
stopped_financial_aid = False
MAIN_PORT = 8888
FA_PORT = 8889
BACKUP_FA_PORT = 8890

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
    random_exit(http_server_fa_main)
    if is_closing:
        tornado.ioloop.IOLoop.instance().stop()
        print('Exit success')


def random_exit(http_server):
    """
    Non-deterministic callback function to generate a new random number
    and potentially exit the financial aid app
    """
    lower = 1
    upper = 1000
    global stopped_financial_aid
    if not stopped_financial_aid:
        if random.randint(lower, upper) > 990:
            http_server.close_all_connections()
            http_server.stop()
            stopped_financial_aid = True
        else:
            pass



class HeartBeatReceiver(tornado.websocket.WebSocketHandler):
    """
    Basic heart beat handler to receive messages from open pages
    """
    def open(self):
        print("Opening heartbeat connection")

    def on_message(self, message):
        if not stopped_financial_aid:
            print(message)
        else:
            print("Financial aid quit unexpectedly")
            self.write_message("stop")
            self.attempt_switch()

    def on_close(self):
        print("Closing heartbeat connection")

    def check_origin(self, origin):
        return True

    def attempt_switch(self):
        """
        Attempt to switch to the passive node
        """
        global http_server_fa_main
        global http_server_fa_backup
        global stopped_financial_aid
        stopped_financial_aid = False

        # Switch to the passive node
        temp_server = http_server_fa_main
        http_server_fa_main = http_server_fa_backup
        http_server_fa_backup = temp_server

        # Restart the backup server
        if not http_server_fa_backup._started:
            http_server_fa_backup.start()

        # Restart the main server
        if not http_server_fa_main._started:
            http_server_fa_main.start()

        # Let the page know to refresh
        self.write_message("start")


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


def make_main_financial_aid_app():
    """
        Create the financial aid app, run based on an empty URL
        :return: The tornado financial aid webapplication
        """
    template_path = os.path.join(os.path.dirname(__file__), "templates")

    static_path = 'static/'
    return tornado.web.Application(
        [
            (r"/financial-aid/", FinancialAidHandler),
            (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': static_path})
        ],
        template_path=template_path,
    )


def make_backup_financial_aid_app():
    """
        Create the backup financial aid app, run based on an empty URL
        :return: The backup tornado financial aid webapplication
        """
    template_path = os.path.join(os.path.dirname(__file__), "templates")

    static_path = 'static/'
    return tornado.web.Application(
        [
            (r"/financial-aid/", FinancialAidHandler),
            (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': static_path})
        ],
        template_path=template_path,
    )

# Run the things!
if __name__ == "__main__":
    app = make_app()
    main_fa_app = make_main_financial_aid_app()
    backup_fa_app = make_backup_financial_aid_app()
    signal.signal(signal.SIGINT, signal_handler)

    # Register the main app
    http_server_main = tornado.httpserver.HTTPServer(app)
    http_server_main.listen(MAIN_PORT)

    # Register the main financial aid app
    http_server_fa_main = tornado.httpserver.HTTPServer(main_fa_app, no_keep_alive=False)
    http_server_fa_main.listen(FA_PORT)

    # Register the backup financial aid app (passive node)
    http_server_fa_backup = tornado.httpserver.HTTPServer(backup_fa_app, no_keep_alive=False)
    http_server_fa_backup.listen(BACKUP_FA_PORT)

    # Register the function to exit tornado, how wonderful that
    # this isn't built in
    tornado.ioloop.PeriodicCallback(try_exit, 100).start()

    print('Starting web server on http://127.0.0.1:8888/ ...')
    print('Starting financial aid web server on http://127.0.0.1:8889/financial-aid/ ...')
    print('Starting backup financial aid web server on http://127.0.0.1:8890/financial-aid/ ...')
    tornado.ioloop.IOLoop.instance().start()
