#!/usr/bin/python3
"""
Unit tests for the Review class.
"""
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_instance_creation(self):
        """Test the creation of a Review instance."""
        instance = Review()
        self.assertIsInstance(instance, Review)
        self.assertTrue(hasattr(instance, "place_id"))
        self.assertTrue(hasattr(instance, "user_id"))
        self.assertTrue(hasattr(instance, "text"))

    def test_attributes(self):
        """Test the attributes of Review instance."""
        instance = Review()
        instance.place_id = "place_123"
        instance.user_id = "user_123"
        instance.text = "Great place!"
        self.assertEqual(instance.place_id, "place_123")
        self.assertEqual(instance.user_id, "user_123")
        self.assertEqual(instance.text, "Great place!")

if __name__ == '__main__':
    unittest.main()
