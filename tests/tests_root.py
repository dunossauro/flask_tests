from unittest import TestCase, mock
from flask import url_for
from app import app


class RootTests(TestCase):
    def setUp(self):
        self.app = app
        self.app.testing = True
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def test_root_deve_retornar_hello_world(self):
        request = self.client.get(url_for('hello'))
        self.assertEqual('Hello World!', request.data.decode())

    def test_root_deve_retornar_status_code_200(self):
        request = self.client.get(url_for('hello'))

        self.assertEqual(200, request.status_code)
