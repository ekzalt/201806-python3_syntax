def splitter(string: str) -> list:
    return list(string)


import unittest


class SplitterTest(unittest.TestCase):
    '''SplitterTest'''

    def testString(self):
        '''testString'''
        actual = splitter('hello')
        expected = ['h', 'e', 'l', 'l', 'o']
        self.assertEqual(actual, expected)

    def testEmpty(self):
        '''testEmpty'''
        actual = splitter('')
        expected = []
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

    # запуск нескольких тестов из фасада
    # suite = unittest.TestSuite([
    #     SplitterTest()
    # ])

    # запуск тестов из консоли
    # python -m unittest .
    # unittest ищет все файлы test_blablabla и запускает
