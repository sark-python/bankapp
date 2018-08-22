from main import db


class Address(db.Model):
    id = db.Column("id", db.Integer, primary_key=True, nullable=False)
    line1 = db.Column("line1", db.String(50), nullable=False)
    line2 = db.Column("line2", db.String(50))
    city = db.Column("city", db.String(20))
    state = db.Column("state", db.String(20))
    country = db.Column("country", db.String(10))
    cust_id = db.Column("cust_id", db.ForeignKey("customer.id"))

