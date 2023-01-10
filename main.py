from config import Config
from create_db import User, Offer, Order
from flask import Flask, jsonify, request
from init_db import db
from create_data import create_data

app = Flask(__name__)


@app.route('/users/', methods=['GET', 'POST'])
def get_all_users():
    if request.method == 'GET':
        users = db.session.query(User).all()

        return jsonify([user.serialize() for user in users])

    elif request.method == 'POST':
        data = request.json
        db.session.add(User(data))
        db.session.commit()


@app.route('/users/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_user_by_id(id):
    if request.method == 'GET':
        user_id = db.session.query(User).filter(User.id == id).first()

        return jsonify(user_id.serialize())

    elif request.method == 'PUT':
        db.session.query(User).filter(User.id == id).update(request.json)
        db.session.commit()

    elif request.method == 'DELETE':
        db.session.query(User).filter(User.id == id).delete()
        db.session.commit()


@app.route('/offers/', methods=['GET', 'POST'])
def get_all_offers():
    if request.method == 'GET':
        offers = db.session.query(Offer).all()

        return jsonify([offer.serialize() for offer in offers])

    elif request.method == 'POST':
        data = request.json
        db.session.add(Offer(data))
        db.session.commit()


@app.route('/offers/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_offer_by_id(id):
    if request.method == 'GET':
        offer_id = db.session.query(Offer).filter(Offer.id == id).first()

        return jsonify(offer_id.serialize())

    elif request.method == 'PUT':
        db.session.query(Offer).filter(Offer.id == id).update(request.json)
        db.session.commit()

    elif request.method == 'DELETE':
        db.session.query(Offer).filter(Offer.id == id).delete()
        db.session.commit()


@app.route('/orders/', methods=['GET', 'POST'])
def get_all_orders():
    if request.method == 'GET':
        orders = db.session.query(Order).all()

        return jsonify([order.serialize() for order in orders])

    elif request.method == 'POST':
        data = request.json
        db.session.add(Order(data))
        db.session.commit()


@app.route('/orders/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_order_by_id(id):
    if request.method == 'GET':
        order_id = db.session.query(Order).filter(Order.id == id).first()

        return jsonify(order_id.serialize())

    elif request.method == 'PUT':
        db.session.query(Order).filter(Order.id == id).update(request.json)
        db.session.commit()

    elif request.method == 'DELETE':
        db.session.query(Order).filter(Order.id == id).delete()
        db.session.commit()


if __name__ == '__main__':
    app.config.from_object(Config())
    db.init_app(app)
    with app.app_context():
        db.drop_all()
        db.create_all()
        create_data()
    app.run(host='localhost', port=5000, debug=True)
