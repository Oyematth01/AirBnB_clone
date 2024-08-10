#!/usr/bin/python3
"""
Unit tests for the User class.
"""
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_instance_creation(self):
        """Test the creation of a User instance."""
        instance = User()
        self.assertIsInstance(instance, User)
        self.assertTrue(hasattr(instance, "email"))
        self.assertTrue(hasattr(instance, "password"))
        self.assertTrue(hasattr(instance, "first_name"))
        self.assertTrue(hasattr(instance, "last_name"))

    def test_attributes(self):
        """Test the attributes of User instance."""
        instance = User()
        instance.email = "user@example.com"
        instance.password = "password"
        instance.first_name = "First"
        instance.last_name = "Last"
        self.assertEqual(instance.email, "user@example.com")
        self.assertEqual(instance.password, "password")
        self.assertEqual(instance.first_name, "First")
        self.assertEqual(instance.last_name, "Last")

if __name__ == '__main__':
    unittest.main()
