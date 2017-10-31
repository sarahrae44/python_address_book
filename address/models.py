from address_book import db

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    address = db.Column(db.String(80))
    city = db.Column(db.String(50))
    state = db.Column(db.String(30))
    zip_code = db.Column(db.String(9))
    live = db.Column(db.Boolean)

    
    
    def __init__(self, name, address, city, state, zip_code, live=True):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.live = live 

        
    def __repr__(self):
        return '<Address %r>' % self.name