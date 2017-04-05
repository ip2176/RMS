from wtforms.fields import IntegerField, StringField, SelectField, DateField
from wtforms.validators import DataRequired, Length
from wtforms_tornado import Form

STATE_CHOICES = [
                 ("AL", "Alabama"), ("AK", "Alaska"), ("AZ", "Arizona"), ("AR", "Arkansas"),
                 ("CA", "California"), ("CO", "Colorado"), ("CT", "Connecticut"), ("DC", "Washington DC"),
                 ("DE", "Delaware"), ("FL", "Florida"), ("GA", "Georgia"),
                 ("HI", "Hawaii"), ("ID", "Idaho"), ("IL", "Illinois"), ("IN", "Indiana"),
                 ("IA", "Iowa"), ("KS", "Kansas"), ("KY", "Kentucky"), ("LA", "Louisiana"),
                 ("ME", "Maine"), ("MD", "Maryland"),
                 ("MA", "Massachusetts"), ("MI", "Michigan"), ("MN", "Minnesota"),
                 ("MS", "Mississippi"), ("MO", "Missouri"), ("MT", "Montana"), ("NE","Nebraska"),
                 ("NV", "Nevada"), ("NH", "New Hampshire"), ("NJ", "New Jersey"),
                 ("NM", "new Mexico"), ("NY", "New York"), ("NC", "North Carolina"),
                 ("ND", "North Dakota"), ("OH", "Ohio"), ("OK", "Oklahoma"), ("OR", "Oregon"),
                 ("PA", "Pennsylvania"), ("RI", "Rhode Island"), ("SC", "South Carolina"),
                 ("SD", "South Dakota"), ("TN", "Tennessee"), ("TX", "Texas"), ("UT", "Utah"),
                 ("VT", "Vermont"), ("VA", "Virginia"), ("WA", "Washington"), ("WV", "West Virginia"),
                 ("WI", "Wisconsin"), ("WY", "Wyoming")
                ]


class PaymentForm(Form):
    """
    Tiny form to get a payment details from the user
    """
    amount = IntegerField(u'Payment Amount', validators=[DataRequired()], render_kw={"placeholder": "$"})
    card_number = StringField(u'Card Number', validators=[DataRequired(), Length(min=16, max=16)],
                              render_kw={"placeholder": "4242-4242-4242-4242"})
    # expiration = DateField(u'Expiration', validators=[DataRequired()])
    ccv = StringField(u'CCV', validators=[DataRequired(), Length(min=3, max=3)], render_kw={"placeholder": "456"})
    name_on_card = StringField(u'Name on Card', validators=[DataRequired(), Length(min=3, max=30)],
                               render_kw={"placeholder": "Jane Doe"})
    address_street_1 = StringField(u'Street Address 1', validators=[DataRequired(), Length(min=5, max=50)],
                                   render_kw={"placeholder": "1 Main st"})
    address_street_2 = StringField(u'Street Address 2 (optional)', validators=[Length(min=5, max=50)],
                                   render_kw={"placeholder": "Apt 2"})
    address_city = StringField(u'City', validators=[DataRequired(), Length(min=3, max=40)],
                               render_kw={"placeholder": "Portland"})
    address_state = SelectField(u'State', choices=STATE_CHOICES, validators=[DataRequired()],
                                render_kw={"placeholder": "State"})
    address_zip = StringField(u'Zip Code', validators=[DataRequired(), Length(min=5, max=9)],
                              render_kw={"placeholder": "12345"})
