import io
import example
import unittest
from unittest.mock import patch

sample_data = io.BytesIO(b"""
    'IBM', 91.1\r
    'AA', 13.25\r
    'MSFT', 27.72\r
""")


class Tests(unittest.TestCase):
    @patch('example.urlopen', return_value=sample_data)
    def test_dowprices(self, mock_urlopen):
        p = example.dowprices()
        self.assertTrue(mock_urlopen.called)
        self.assertEqual(p, {'IBM': 91.1, 'AA': 13.25, 'MSFT': 27.72})


if __name__ == '__main__':
    unittest.main()
