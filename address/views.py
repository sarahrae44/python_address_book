from address_book import app
from flask import render_template, redirect, flash, url_for
from address_book import db
from address.models import Address
from address.form import AddressForm

@app.route('/')
@app.route('/index')
def index():
    addresses = Address.query.filter_by(live=True).order_by(Address.state.asc())
    return render_template('address/addresses.html', addresses=addresses)

@app.route('/address', methods=('GET', 'POST'))
def address():
    form = AddressForm()
    if form.validate_on_submit():
        name = form.name.data
        address = form.address.data
        city = form.city.data
        state = form.state.data
        zip_code = form.zip_code.data
        address = Address(name, address, city, state, zip_code)
        db.session.add(address)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('address/address.html', form=form)
    
@app.route('/delete/<int:address_id>')
def delete(address_id):
    address = Address.query.filter_by(id=address_id).first_or_404()
    address.live = False
    db.session.commit()
    flash("Entry deleted")
    return redirect('/index')    
