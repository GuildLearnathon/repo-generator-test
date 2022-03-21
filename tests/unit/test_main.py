from unittest import TestCase
from main import hello


class TestMain(TestCase):
    def test_hello_returns_string_with_name_injected(self):
        name = "Ginny Weasley"
        expected = "Hello Ginny Weasley!"
        actual = hello(name)

        self.assertEqual(expected, actual)