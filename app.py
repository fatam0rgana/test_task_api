from application import app, db
from application.models.currency_model import Currency


if __name__ == '__main__':
    app.run(debug=True)

