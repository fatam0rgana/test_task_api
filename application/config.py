import os

SECRET_KEY = '\xf0?a\x9a\\\xff\xd4;\x0c\xcbHi'
SQLALCHEMY_DATABASE_URI = 'sqlite:///sql/test_task.db'
secret = os.environ.get('SHOP_SECRET')
shop_id = os.environ.get('SHOP_ID')