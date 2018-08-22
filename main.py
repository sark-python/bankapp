from main import app, db
from main.models import customer, address
from main.service import customerservice

if __name__ == '__main__' :
    db.create_all()
    app.run(debug=True)