from application import app, db
from application.models.currency_model import Currency


if __name__ == '__main__':
    db.create_all()
    try:
        cur1 = Currency(currency_name='RUB', currency_value=643)
        cur2 = Currency(currency_name='USD', currency_value=840)
        cur3 = Currency(currency_name='EUR', currency_value=978)
        db.session.add(cur1)
        db.session.add(cur2)
        db.session.add(cur3)
        db.session.commit()
    except:
        pass
    app.run(debug=False)

