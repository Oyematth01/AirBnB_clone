#!/usr/bin/python3
"""
Unit tests for the Place class.
"""
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_instance_creation(self):
        """Test the creation of a Place instance."""
        instance = Place()
        self.assertIsInstance(instance, Place)
        self.assertTrue(hasattr(instance, "city_id"))
        self.assertTrue(hasattr(instance, "user_id"))
        self.assertTrue(hasattr(instance, "name"))
        self.assertTrue(hasattr(instance, "description"))
        self.assertTrue(hasattr(instance, "number_rooms"))
        self.assertTrue(hasattr(instance, "number_bathrooms"))
        self.assertTrue(hasattr(instance, "max_guest"))
        self.assertTrue(hasattr(instance, "price_by_night"))
        self.assertTrue(hasattr(instance, "latitude"))
        self.assertTrue(hasattr(instance, "longitude"))

    def test_attributes(self):
        """Test the attributes of Place instance."""
        instance = Place()
        instance.city_id = "city_123"
        instance.user_id = "user_123"
        instance.name = "Cool Place"
        instance.description = "A very cool place."
        instance.number_rooms = 3
        instance.number_bathrooms = 2
        instance.max_guest = 4
        instance.price_by_night = 100
        instance.latitude = 37.7749
        instance.longitude = -122.4194
        self.assertEqual(instance.city_id, "city_123")
        self.assertEqual(instance.user_id, "user_123")
        self.assertEqual(instance.name, "Cool Place")
        self.assertEqual(instance.description, "A very cool place.")
        self.assertEqual(instance.number_rooms, 3)
        self.assertEqual(instance.number_bathrooms, 2)
        self.assertEqual(instance.max_guest, 4)
        self.assertEqual(instance.price_by_night, 100)
        self.assertEqual(instance.latitude, 37.7749)
        self.assertEqual(instance.longitude, -122.4194)

if __name__ == '__main__':
    unittest.main()
