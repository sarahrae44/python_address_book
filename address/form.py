from flask_wtf import Form
from wtforms import validators, StringField

class AddressForm(Form):
    name = StringField('Name', [
        validators.Required(),
        validators.Length(max=80)
        ])
    address = StringField('Address', [
        validators.Required(),
        validators.Length(max=80)
        ])
    city = StringField('City', [
        validators.Required(),
        validators.Length(max=50)
        ])    
    state = StringField('State', [
        validators.Required(),
        validators.Length(max=30)
        ])
    zip_code = StringField('Zip Code', [
        validators.Required(),
        validators.Length(max=9)
        ])   
    