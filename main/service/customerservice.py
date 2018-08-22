from main import app
from flask import request
from main.impl import customerserviceimpl


@app.route("/add", methods=['POST'])
def add_customer():
    data = request.get_json()
    return customerserviceimpl.addcustomer(data)
