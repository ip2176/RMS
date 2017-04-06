from .forms import PaymentForm
from tornado import web, template, escape
import json
import os

balance = 126000
payment_success = False
template_loader = template.Loader(os.path.join(os.path.dirname(__file__), "templates"))


class FinancialAidHandler(web.RequestHandler):
    """
    Basic hello world implementation of a FA handler class
    """

    def get(self):
        global balance
        global payment_success
        form = PaymentForm()
        payment_success = False
        result = template_loader.load("financial_aid.html").generate(title="[RMS] Financial Aid",
                                                                     form=form, balance=balance,
                                                                     payment_success=payment_success,
                                                                     make_payment=False)
        self.write(result)

    def post(self):
        global balance
        global payment_success
        body = self.request.body.decode()

        # The user selected to make a payment, show them the form
        if 'make_payment' in body:
            form = PaymentForm()
            payment_success = False
            result = template_loader.load("financial_aid.html").generate(title="[RMS] Financial Aid",
                                                                         form=form, balance=balance,
                                                                         payment_success=payment_success,
                                                                         make_payment=True)
            self.write(result)

        # The user submitted the form, check it
        else:
            form = PaymentForm(self.request.arguments)
            if form.validate():
                balance = balance - form.data['amount']
                payment_success = True
                result = template_loader.load("financial_aid.html").generate(title="[RMS] Financial Aid",
                                                                             form=form, balance=balance,
                                                                             amount=form.data['amount'],
                                                                             payment_success=payment_success,
                                                                             make_payment=True)
                self.write(result)
            else:
                self.set_status(400)
                self.write("There were errors on the form: {}".format(form.errors))
