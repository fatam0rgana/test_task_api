from flask import render_template, url_for, flash, request
from application import app, db
from application.config import secret, shop_id
from application.service.data_handling import data_to_hash, generate_uuid
from application.models.payments_model import Payments


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        amount = request.form['amount']
        currency = request.form['currency']
        description = request.form['description']
        data = {'amount': amount, 'currency': currency, 'shop_id': shop_id, 'description': description, \
                'shop_order_id': str(generate_uuid())}
        if currency == '643':
            data['payway'] = 'advcash_rub'
            required_keys = ("shop_id", "payway", "amount", "currency", "shop_order_id")
            data_to_hash(data, required_keys, secret)
        elif currency == '840':
            pass
        elif currency == '978':
            required_keys = ('amount', 'currency', 'shop_id', 'shop_order_id')
            data_to_hash(data, required_keys, secret)
    return render_template('index.html')
