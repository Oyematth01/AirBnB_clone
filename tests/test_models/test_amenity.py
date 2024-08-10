#!/usr/bin/python3
"""
Unit tests for the Amenity class.
"""
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_instance_creation(self):
        """Test the creation of an Amenity instance."""
        instance = Amenity()
        self.assertIsInstance(instance, Amenity)
        self.assertTrue(hasattr(instance, "name"))

    def test_attributes(self):
        """Test the attributes of Amenity instance."""
        instance = Amenity()
        instance.name = "WiFi"
        self.assertEqual(instance.name, "WiFi")

if __name__ == '__main__':
    unittest.main()
