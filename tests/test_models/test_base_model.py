#!/usr/bin/python3
from models.base_model import BaseModel
import unittest

class TestBaseModel(unittest.TestCase):

    def test_save(self):
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(initial_updated_at, model.updated_at)

    def test_str(self):
        model = BaseModel()
        self.assertTrue(model.__str__)

if __name__ == "__main__":
    unittest.main()
