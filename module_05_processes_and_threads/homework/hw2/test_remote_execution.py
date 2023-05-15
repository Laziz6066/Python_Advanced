import unittest
from remote_execution import app


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.testing = True
        self.client = self.app.test_client()

    def test_run_code_valid_input(self):
        with self.app.test_request_context('/run_code', method='POST',
                                           data={'code': 'print("Hello, World!")', 'timeout': 5}):
            response = self.client.post('/run_code')
            data = response.get_json()

            self.assertEqual(response.status_code, 200)
            self.assertIn('output', data)
            self.assertEqual(data['output'], 'Hello, World!\n')

    def test_run_code_invalid_input(self):
        with self.app.test_request_context('/run_code', method='POST',
                                           data={'code': 'print("Hello, World!")', 'timeout': 'abc'}):
            response = self.client.post('/run_code')
            data = response.get_json()

            self.assertEqual(response.status_code, 400)
            self.assertIn('error', data)
            self.assertEqual(data['error'], 'Invalid input')


if __name__ == '__main__':
    unittest.main()
