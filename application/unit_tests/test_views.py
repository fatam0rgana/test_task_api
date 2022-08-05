import http
from datetime import datetime
from application import app, db
from application.models.payments_model import Payments
from base_test import BaseTestCase


class TestHomePage(BaseTestCase):
    """
    This is the class for home view test case
    """

    def test_home_page(self):
        """
        Testing / page

        """
        client = app.test_client()
        response1 = client.get('/')
        assert response1.status_code == http.HTTPStatus.OK

    def test_eur_page(self):
        """
        Testing /eur page
        """
        client = app.test_client()
        response1 = client.get('/eur')
        assert response1.status_code == http.HTTPStatus.OK

    def test_adding_to_db(self):
        """
        Testing adding new records to database
        """
        client = app.test_client()
        new_row = Payments(amount=1, currency=840, description='qwe', shop_order_id='ewq',
                           sign='123', created=datetime.now())
        db.session.add(new_row)
        db.session.commit()
        self.assertEqual(1, Payments.query.count())