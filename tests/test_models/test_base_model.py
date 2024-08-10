#!/usr/bin/python3
"""
Unit tests for the BaseModel class.
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def test_instance_creation(self):
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_to_dict(self):
        instance = BaseModel()
        dict_repr = instance.to_dict()
        self.assertEqual(dict_repr["__class__"], "BaseModel")
        self.assertEqual(dict_repr["id"], instance.id)
        self.assertEqual(dict_repr["created_at"], instance.created_at.isoformat())
        self.assertEqual(dict_repr["updated_at"], instance.updated_at.isoformat())

    def test_save(self):
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(old_updated_at, instance.updated_at)

if __name__ == '__main__':
    unittest.main()
