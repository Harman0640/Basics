"""Tests for the application entry point."""

import unittest

from src.basic_python.main import greet


class GreetTests(unittest.TestCase):
    def test_greet_returns_expected_message(self) -> None:
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_greet_removes_surrounding_whitespace(self) -> None:
        self.assertEqual(greet("  Ada  "), "Hello, Ada!")

    def test_greet_rejects_an_empty_name(self) -> None:
        with self.assertRaisesRegex(ValueError, "Name cannot be empty"):
            greet("   ")


if __name__ == "__main__":
    unittest.main()
