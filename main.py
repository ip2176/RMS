import tornado.ioloop
import tornado.web
import signal

# Global variable used to figure out if we are exiting the app or not
is_closing = False


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


class MainHandler(tornado.web.RequestHandler):
    """
    Basic hello world implementation of a main handler class
    """
    def get(self):
        self.write("Hello, world")


def make_app():
    """
    Create the main app, run based on an empty URL
    :return: The tornado webapplication
    """
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

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
