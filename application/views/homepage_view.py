import requests
import json
from datetime import datetime
from flask import render_template, url_for, flash, request, redirect
from application import app, db
from application.config import secret, shop_id
from application.service.data_handling import data_to_hash, generate_uuid
from application.service.validation import *
from application.models.payments_model import Payments
from application.models.currency_model import Currency


@app.route("/eur", methods=["POST", "GET"])
def pay_eur():
    if request.method == 'GET':
        amount = request.args.get('amount')
        currency = request.args.get('currency')
        shop_id = request.args.get('shop_id')
        shop_order_id = request.args.get('shop_order_id')
        sign = request.args.get('sign')
    return render_template('pay_eur.html', amount=amount, currency=currency, shop_id=shop_id,
                           shop_order_id=shop_order_id, sign=sign)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        redirect_link = url_for('index')
        amount = request.form["amount"]
        currency = request.form["currency"]
        description = request.form["description"]
        if validate_amount(amount) and validate_currency(currency):
            data = {"amount": amount, "currency": currency, "shop_id": shop_id, "description": description,
                    "shop_order_id": str(generate_uuid())}
            if currency == "643":
                data["payway"] = "advcash_rub"
                required_keys = ("shop_id", "payway", "amount", "currency", "shop_order_id")
                data_to_hash(data, required_keys, secret)
                r = requests.post(url="https://core.piastrix.com/invoice/create", data=json.dumps(data),
                                  headers={"Content-Type": "application/json"})
                if r.json()['data'] and r.json()['result']:
                    redirect_link = r.json()['data']['url']
                else:
                    flash(r.json()['message'], 'alert-danger')
            elif currency == "840":
                data["shop_currency"] = 840
                data["payer_currency"] = 840
                data["shop_amount"] = amount
                required_keys = ("shop_amount", "shop_currency", "shop_id", "shop_order_id", "payer_currency")
                data_to_hash(data, required_keys, secret)
                r = requests.post(url="https://core.piastrix.com/bill/create", data=json.dumps(data),
                                  headers={"Content-Type": "application/json"})
                if r.json()['data'] and r.json()['result']:
                    redirect_link = r.json()['data']['url']
                else:
                    flash(r.json()['message'], 'alert-danger')
            elif currency == "978":
                required_keys = ("amount", "currency", "shop_id", "shop_order_id")
                data_to_hash(data, required_keys, secret)
                redirect_link = f"/eur?amount={amount}&currency=978&shop_id={shop_id}" \
                                + f"&shop_order_id={data.get('shop_order_id')}&sign={data.get('sign')}"
            new_record = Payments(amount=amount, currency=currency, description=description,
                                  shop_order_id=data.get("shop_order_id"), sign=data.get("sign"),
                                  created=datetime.now())
            db.session.add(new_record)
            db.session.commit()
            return redirect(redirect_link)
        else:
            flash('You entered invalid data, try again', 'alert-danger')
    return render_template("index.html", currencies=Currency.query.all())
