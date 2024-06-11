import sqlalchemy as db

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:pwd123@0.0.0.0/himanshu'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pwd123@psql-db:5432/himanshu'
db = SQLAlchemy(app)

class User(db.Model):
    email = db.Column(db.String, primary_key=True, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

class Car(db.Model):
    model_id = db.Column(db.Integer, primary_key = True)
    model_name = db.Column(db.String(50), nullable = False)
    category_name = db.Column(db.String(50), db.ForeignKey('category.name'), nullable = False)

class Category(db.Model):
    name = db.Column(db.String(50), primary_key = True, nullable = False)
    cars = db.relationship('Car', backref = 'category')

with app.app_context():
    db.create_all()

    # ----Insert----
    sedan = Category(name="sedan")
    hatchback = Category(name="hatchback")

    virtus = Car(model_id=1234, model_name = "virtus", category_name = "sedan")
    polo = Car(model_id=1235, model_name = "polo", category_name = "hatchback")

    db.session.add(sedan)
    db.session.add(hatchback)

    db.session.add(virtus)
    db.session.add(polo)
    

    try:
        db.session.commit()
    except Exception as e: 
        print(e)
        db.session.rollback()
    finally:
        db.session.close()
  

    # ----GET-----
    print(Car.query.all())
    print(Car.query.first())
    #polo = Car.query.get(1235)
    #print(polo.model_id, polo.model_name, polo.category_name)

    q1 = Car.query.filter(Car.model_name == "virtus").first()
    print(q1.model_name, q1.category_name)

    # ----UPDATE/DELETE----
    #polo.model_name = "polo gt"
    db.session.commit()
    #db.session.delete(polo)
    db.session.commit()

@app.route("/") 
def hello():
    return "Starting flask...!"

@app.route("/<my_space>") 
def route2(my_space):
    return "Inside dynamic route...!.."+my_space

@app.route('/page/<int:num>') 
def calculate_square(num):
    return "square of "+str(num) + " is: "+ str(num*num)

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 3000)