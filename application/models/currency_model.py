from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from application import db, app

ma = Marshmallow(app)


class Currency(db.Model):
    currency_name = db.Column(db.String(4), nullable=False)
    currency_value = db.Column(db.Integer, nullable=False, primary_key=True)

    def __repr__(self):
        return self.currency_value


class DepartmentsSchema(ma.Schema):
    class Meta:
        fields = ('currency_id', 'currency_name', 'currency_value')
