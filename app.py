from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:oxbridge123@localhost/p'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone_no = db.Column(db.String(15))  # New column for phone number

@app.route("/add_item", methods=["POST"])
def add_item():
    data = request.json
    new_item = Item(phone_no=data.get("phone_no"))
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"message": "Item added successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
