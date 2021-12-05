# To test the exception's value
import errno
import unittest


# A simple function to illustrate
def parse_int(s):
    return int(s)


class TestIO(unittest.TestCase):
    def test_file_not_found(self):
        try:
            f = open('example.py')
        except IOError as e:
            self.assertEqual(e.errno, errno.ENOENT)
        else:
            self.fail('IOError not raised')


class TestConversion(unittest.TestCase):
    def test_bad_int(self):
        try:
            r = parse_int('N/A')
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
        else:
            self.fail('ValueError not raised')


# Testing the value of Exception raised
class TestConversion2(unittest.TestCase):
    def test_bad_int(self):
        self.assertRaisesRegex(ValueError, 'invalid literal .*', parse_int, 'N/A')
