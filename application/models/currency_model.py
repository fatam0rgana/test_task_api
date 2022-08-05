from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from application import db, app

ma = Marshmallow(app)


class Currency(db.Model):
    currency_id = db.Column(db.Integer, primary_key=True)
    currency_name = db.Column(db.String(4), nullable=False)
    currency_value = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return self.currency_id


class DepartmentsSchema(ma.Schema):
    class Meta:
        fields = ('currency_id', 'currency_name', 'currency_value')
