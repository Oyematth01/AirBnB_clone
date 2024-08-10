#!/usr/bin/python3
"""
Unit tests for the FileStorage class.
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import json

class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Set up test environment."""
        self.storage = FileStorage()
        self.model = BaseModel()

    def tearDown(self):
        """Tear down test environment."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test the all method."""
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new(self):
        """Test the new method."""
        self.storage.new(self.model)
        key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test the save method."""
        self.storage.new(self.model)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """Test the reload method."""
        self.storage.new(self.model)
        self.storage.save()
        self.storage.reload()
        key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
        self.assertIn(key, self.storage.all())

if __name__ == '__main__':
    unittest.main()
