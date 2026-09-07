"""Tests for the application entry point."""

import unittest

from src.basic_python.main import greet


class GreetTests(unittest.TestCase):
    def test_greet_returns_expected_message(self) -> None:
        self.assertEqual(greet("Ada"), "Hello, Ada!")


if __name__ == "__main__":
    unittest.main()
