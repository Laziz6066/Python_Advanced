from unittest import TestCase, main
from module_03_ci_culture_beginning.homework.hw2.decrypt import decrypt


class TestDecrypt(TestCase):
    def test_decrypt(self):
        self.assertEqual(decrypt("абра-кадабра."), "абра-кадабра")
        self.assertEqual(decrypt("абраа..-кадабра"), "абра-кадабра")
        self.assertEqual(decrypt("абраа..-.кадабра"), "абра-кадабра")
        self.assertEqual(decrypt("абра--..кадабра"), "абра-кадабра")
        self.assertEqual(decrypt("абрау...-кадабра"), "абра-кадабра")
        self.assertEqual(decrypt("абра........"), "")
        self.assertEqual(decrypt("абр......a."), "a")
        self.assertEqual(decrypt("1..2.3"), "23")
        self.assertEqual(decrypt("."),  "")
        self.assertEqual(decrypt("1......................."), "")
# TODO стоило поместить все исходные данные для тестирования в словарь или список списков и выполнить все "кейсы"
#  в цикле


if __name__ == '__main__':
    main()