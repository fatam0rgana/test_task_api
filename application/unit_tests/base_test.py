import unittest
from application import app, db


class BaseTestCase(unittest.TestCase):
    """

    Base test case class
    """

    def setUp(self):
        """

        Execute before test
        """
        self.app = app
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sql/test_task_testdb.db'
        self.app.config['TESTING'] = True
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self) -> None:
        """

        Execute after test

        """
        db.session.remove()
        db.drop_all()
