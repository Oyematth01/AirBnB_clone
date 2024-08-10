#!/usr/bin/python3
"""
Unit tests for the State class.
"""
import unittest
from models.state import State

class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_instance_creation(self):
        """Test the creation of a State instance."""
        instance = State()
        self.assertIsInstance(instance, State)
        self.assertTrue(hasattr(instance, "name"))

    def test_attributes(self):
        """Test the attributes of State instance."""
        instance = State()
        instance.name = "California"
        self.assertEqual(instance.name, "California")

if __name__ == '__main__':
    unittest.main()
