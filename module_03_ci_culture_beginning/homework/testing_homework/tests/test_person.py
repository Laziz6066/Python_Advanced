import unittest
from datetime import datetime
from module_03_ci_culture_beginning.homework.hw4.person import Person


class TestPerson(unittest.TestCase):
    def test_get_age(self):
        p = Person('John', 1990, '123 Main St.')
        self.assertEqual(p.get_age(), datetime.now().year - 1990)

    def test_set_name(self):
        p = Person('John', 1990, '123 Main St.')
        p.set_name('Jane')
        self.assertEqual(p.get_name(), 'Jane')

    def test_set_address(self):
        p = Person('John', 1990, '123 Main St.')
        p.set_address('456 Elm St.')
        self.assertEqual(p.get_address(), '456 Elm St.')

    def test_is_homeless(self):
        p = Person('John', 1990)
        self.assertTrue(p.is_homeless())

        p.set_address('123 Main St.')
        self.assertFalse(p.is_homeless())


if __name__ == '__main__':
    unittest.main()
