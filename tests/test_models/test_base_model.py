#!/usr/bin/python3
"""
Unit tests for the BaseModel class.
"""
import unittest
import time
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_instance_creation(self):
        """Test the creation of a BaseModel instance."""
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_to_dict(self):
        """Test the to_dict method."""
        instance = BaseModel()
        dict_repr = instance.to_dict()
        self.assertEqual(dict_repr["__class__"], "BaseModel")
        self.assertEqual(dict_repr["id"], instance.id)
        self.assertEqual(dict_repr["created_at"], instance.created_at.isoformat())
        self.assertEqual(dict_repr["updated_at"], instance.updated_at.isoformat())

    def test_save(self):
        """Test the save method."""
        instance = BaseModel()
        old_updated_at = instance.updated_at
        time.sleep(1)  # Ensure there is a noticeable time difference
        instance.save()
        self.assertNotEqual(old_updated_at, instance.updated_at)
    
	def test_str(self):
        """Test the __str__ method."""
        instance = BaseModel()
        expected_str = "[BaseModel] ({}) {{'id': '{}', 'created_at': '{}', 'updated_at': '{}'}}".format(
            instance.id,
            instance.id,
            instance.created_at.isoformat(),
            instance.updated_at.isoformat()
        )
        self.assertEqual(str(instance), expected_str)

if __name__ == '__main__':
    unittest.main()
