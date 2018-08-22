from main.models.customer import Customer, CustomerSchema
from main import db
from flask import jsonify


def addcustomer(data):

    name = data["name"]
    age = data["age"]

    cust = Customer(name=name, age=age)
    db.session.add(cust)
    db.session.commit()

    check = Customer.query.filter_by(name=name).first()
    schema = CustomerSchema()
    result = schema.dump(check)
    return jsonify(result)
