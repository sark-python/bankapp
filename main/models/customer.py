from main import db
from marshmallow import Schema

class Customer(db.Model):
    id = db.Column("id", db.Integer, primary_key=True, nullable=False)
    name = db.Column("name", db.String(20), nullable=False)
    age = db.Column("age", db.Integer, nullable=False)
    addresses = db.relationship("Address", backref="customer")

    def __repr__(self):
        return "\{ 'name':'{}', 'age':'{}' \}".format(self.name,self.age);


class CustomerSchema(Schema):
    class Meta:
        fields = ('name', 'age')
