import unittest
from block_errors import BlockErrors


class BlockErrorsTest(unittest.TestCase):

    def test_block_errors(self):

        err_types = {ZeroDivisionError, TypeError}
        try:
            with BlockErrors(err_types):
                a = 1 / 0
            self.fail('Тест 1: Выполнено без ошибок')
        except Exception as e:
            self.fail(f'Тест 1: Ошибка: {type(e).__name__}: {str(e)}')

        err_types = {ZeroDivisionError}
        try:
            with BlockErrors(err_types):
                a = 1 / '0'
            self.fail('Тест 2: Выполнено без ошибок')
        except Exception as e:
            self.fail(f'Тест 2: Ошибка: {type(e).__name__}: {str(e)}')

        outer_err_types = {TypeError}
        try:
            with BlockErrors(outer_err_types):
                inner_err_types = {ZeroDivisionError}
                try:
                    with BlockErrors(inner_err_types):
                        a = 1 / '0'
                    self.fail('Тест 3: Внутренний блок: выполнено без ошибок')
                except Exception as e:
                    self.fail(f'Тест 3: Внутренний блок: ошибка: {type(e).__name__}: {str(e)}')
            self.fail('Тест 3: Внешний блок: выполнено без ошибок')
        except Exception as e:
            self.fail(f'Тест 3: Внешний блок: ошибка: {type(e).__name__}: {str(e)}')

        err_types = {Exception}
        try:
            with BlockErrors(err_types):
                a = 1 / '0'
            self.fail('Тест 4: Выполнено без ошибок')
        except Exception as e:
            self.fail(f'Тест 4: Ошибка: {type(e).__name__}: {str(e)}')


if __name__ == '__main__':
    unittest.main()
