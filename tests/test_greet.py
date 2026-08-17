import unittest

from greet import greet


class TestGreet(unittest.TestCase):
    def test_greet_returns_expected_message(self):
        self.assertEqual(greet("World"), "Hello, World!")

    def test_greet_with_different_name(self):
        self.assertEqual(greet("Austin"), "Hello, Austin!")


if __name__ == "__main__":
    unittest.main()
