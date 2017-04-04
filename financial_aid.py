import tornado.web


class FinancialAidHandler(tornado.web.RequestHandler):
    """
    Basic hello world implementation of a FA handler class
    """
    def get(self):
        self.render("financial_aid.html", title="[RMS] Financial Aid")
