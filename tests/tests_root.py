from unittest import TestCase, mock
from flask import url_for
from app import app


class RootTests(TestCase):
    def setUp(self):
        self.app = app
        self.app.config["SERVER_NAME"] = "localhost:5000"
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.app.testing = True

    def test_root_should_return_hello_world(self):
        expected = 'Hello World!'
        request = self.client.get(url_for('hello'))

        self.assertEqual(expected, request.data.decode())

    def test_root_should_return_200_in_GET_request(self):
        expected = 200
        request = self.client.get(url_for('hello'))

        self.assertEqual(expected, request.status_code)
