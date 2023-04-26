from unittest import TestCase, main
from freezegun import freeze_time
from module_03_ci_culture_beginning.homework.hw1.hello_word_with_day import hello_world, app
import datetime


class TestHelloWorld(TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    def test_can_get_correct_usernae(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

    def test_can_get_correct_username_with_week_date(self):
        username = 'Good Wednesday'
        with freeze_time("2022-05-04"):
            response = self.app.get(self.base_url + username)
            response_text = response.data.decode()
            self.assertIn('Wednesday', response_text)


if __name__ == '__main__':
    main()