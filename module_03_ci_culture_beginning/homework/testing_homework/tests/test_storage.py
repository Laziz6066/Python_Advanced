from unittest import TestCase, main
from module_03_ci_culture_beginning.homework.hw3.storage import app, add, calculate_year, calculate_month
import datetime


class TestStorage(TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.client = app.test_client()
        self.date = datetime.date.today().isoformat()
        self.number = 42
        self.total = 150

    def test_add_correct_date(self):
        with self.assertRaises(ValueError) as c:
            add('978456', 1500)
        self.assertEqual("Incorrect data format, should be YYYY-MM-DD", c.exception.args[0])

    def test_add_valid_date(self):
        response = self.client.get(f"/add/{self.date}/{self.number}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Record successfully added.')

    def test_calculate_year_valid(self):
        response = self.client.get('/calculate/2022')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Total amount for 2022 is 0 rub.')

    def test_calculate_year_invalid(self):
        response = self.client.get('/calculate/abcd')
        self.assertEqual(response.status_code, 404)

    def test_calculate_year_no_data(self):
        response = self.client.get('/calculate/2030')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Total amount for 2030 is 0 rub.')

    def test_calculate_month_valid(self):
        response = self.client.get('/calculate/2023/01')
        self.assertEqual(response.status_code, 200)
        print(response.data)
        self.assertEqual(response.data, b'Total amount for 2023-01 is 120 rub.')

    def test_calculate_month_invalid_month(self):
        response = self.client.get('/calculate/2022/13')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'No data available for the given year and month.')

    def test_calculate_month_invalid_year(self):
        response = self.client.get('/calculate/abcd/1')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    main()
