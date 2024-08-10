#!/usr/bin/python3
"""
Unit tests for the City class.
"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_instance_creation(self):
        """Test the creation of a City instance."""
        instance = City()
        self.assertIsInstance(instance, City)
        self.assertTrue(hasattr(instance, "state_id"))
        self.assertTrue(hasattr(instance, "name"))

    def test_attributes(self):
        """Test the attributes of City instance."""
        instance = City()
        instance.state_id = "state_123"
        instance.name = "San Francisco"
        self.assertEqual(instance.state_id, "state_123")
        self.assertEqual(instance.name, "San Francisco")

if __name__ == '__main__':
    unittest.main()
