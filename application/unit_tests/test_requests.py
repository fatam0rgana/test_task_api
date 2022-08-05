import http
from urllib import response
import requests
import json
from application import app, db
from base_test import BaseTestCase


class TestRequestsAndRedirects(BaseTestCase):
    """
    This is the class for requuests tests
    P.S.: I dont know how to mock(:
    """

    def test_usd_payment(self):
        """
        Testing api responce for usd payments
        """
        data = {'amount': '1', 'currency': '840', 'shop_id': '5', 'description': 'qwe',
                'shop_order_id': '5749aa63-5a24-4b9e-a337-498442c445ff', 'shop_currency': 840,
                'payer_currency': 840, 'shop_amount': '1',
                'sign': 'e981d9cf538bbb0e74db1a2c5d49074797650b8a535486ebcb49aedd5c78059f'}
        r = requests.post(url="https://core.piastrix.com/bill/create", data=json.dumps(data),
                          headers={"Content-Type": "application/json"})
        assert r.json()['data']
        data = {'amount': 'qwe', 'currency': 'qwe', 'shop_id': 'qwe', 'description': 'qwe',
                'shop_order_id': 'qwe', 'shop_currency': 840,
                'payer_currency': 840, 'shop_amount': '1',
                'sign': 'qwe'}
        r = requests.post(url="https://core.piastrix.com/bill/create", data=json.dumps(data),
                          headers={"Content-Type": "application/json"})
        assert not r.json()['data']


    def test_rub_payment(self):
        data = {'amount': '1', 'currency': '643', 'shop_id': '5', 'description': '',
                'shop_order_id': '386cea92-12f0-4f5b-99cb-b0746f2ae7b8', 'payway': 'advcash_rub',
                'sign': '8f8c95a5551951e7c0b4487a3d9cc4c4eb5c945f28621e220e13618deb586ad9'}
        r = requests.post(url="https://core.piastrix.com/invoice/create", data=json.dumps(data),
                          headers={"Content-Type": "application/json"})
        assert not r.json()['data']
