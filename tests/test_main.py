import unittest

from create_box import create_box

first_box_expected = """
****
****
****
""".lstrip()

second_box_expected = """
@
""".lstrip()

third_box_expected = """
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
""".lstrip()


class TestCreateBox(unittest.TestCase):
    def test_box(self):
        self.assertEqual(create_box(3, 4, '*'), first_box_expected)
        
    def test_third_box(self):
        self.assertEqual(create_box(3, 24, 'x'), third_box_expected)

    def test_small_box(self):
        self.assertEqual(create_box(1, 1, '@'), second_box_expected)
        
    def test_invalid_size(self):
        self.assertEqual(create_box(0, 1, '@'), 'invalid size')
        
    def test_invalid_size_two(self):
        self.assertEqual(create_box(1, 0, '@'), 'invalid size')

    # Add your own test using third_box_expected
from create_box import empty_box

first_empty_box_expected = """
***
* *
***
""".lstrip()

class TestCreateEmptyBox(unittest.TestCase):
    def test_empty_box(self):
        self.assertEqual(empty_box(3, 3, '*'), first_empty_box_expected)