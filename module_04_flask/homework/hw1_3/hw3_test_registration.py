"""
Для каждого поля и валидатора в эндпоинте /registration напишите юнит-тест,
который проверит корректность работы валидатора. Таким образом, нужно проверить, что существуют наборы данных,
которые проходят валидацию, и такие, которые валидацию не проходят.
"""

import unittest
from flask import Flask
from flask_testing import TestCase
from hw1_registration import app, RegistrationForm


class RegistrationFormTestCase(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_valid_email(self):
        with self.app.test_client() as client:
            response = client.post('/registration', data={'email': 'valid@example.com'})
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Successfully registered', response.data)

    def test_invalid_email(self):
        with self.app.test_client() as client:
            response = client.post('/registration', data={'email': 'invalid'})
            self.assertEqual(response.status_code, 400)
            self.assertIn(b'Invalid input', response.data)

    def test_valid_phone(self):
        with self.app.test_client() as client:
            response = client.post('/registration', data={'phone': '1234567890'})
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Successfully registered', response.data)

    def test_invalid_phone(self):
        with self.app.test_client() as client:
            response = client.post('/registration', data={'phone': '12345'})
            self.assertEqual(response.status_code, 400)
            self.assertIn(b'Invalid input', response.data)

    def test_valid_name(self):
        with self.app.test_client() as client:
            response = client.post('/registration', data={'name': 'John Doe'})
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Successfully registered', response.data)

    def test_invalid_name(self):
        with self.app.test_client() as client:
            response = client.post('/registration', data={'name': ''})
            self.assertEqual(response.status_code, 400)
            self.assertIn(b'Invalid input', response.data)

    def test_valid_address(self):
        with self.app.test_client() as client:
            response = client.post('/registration', data={'address': '123 Main St'})
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Successfully registered', response.data)

    def test_invalid_address(self):
        with self.app.test_client() as client:
            response = client.post('/registration', data={'address': ''})
            self.assertEqual(response.status_code, 400)
            self.assertIn(b'Invalid input', response.data)

    def test_valid_index(self):
        with self.app.test_client() as client:
            response = client.post('/registration', data={'index': '12345'})
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Successfully registered', response.data)

    def test_invalid_index(self):
        with self.app.test_client() as client:
            response = client.post('/registration', data={'index': '123'})
            self.assertEqual(response.status_code, 400)
            self.assertIn(b'Invalid input', response.data)

    def test_valid_comment(self):
        with self.app.test_client() as client:
            response = client.post('/registration', data={'comment': 'Some comment'})
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Successfully registered', response.data)

    def test_no_comment(self):
        with self.app.test_client() as client:
            response = client.post('/registration')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Successfully registered', response.data)


if __name__ == '__main__':
    unittest.main()

