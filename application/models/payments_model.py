from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from application import db, app
from application.models.currency_model import Currency

ma = Marshmallow(app)


class Payments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.Integer, db.ForeignKey('currency.currency_value'), nullable=False)
    description = db.Column(db.String(150))
    shop_order_id = db.Column(db.String(255), nullable=False)
    sign = db.Column(db.String(150), nullable=False)
    created = db.Column(db.DateTime)

    def __repr__(self):
        return str(self.id)


class DepartmentsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'amount', 'currency', 'description', 'shop_order_id', 'sign')
