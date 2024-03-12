#!/usr/bin/python3
from models.base_model import BaseModel
import unittest

class TestBaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.model = BaseModel()
        cls.model.name = "Gerges"
        cls.model.my_number = 24


    def test_save(self):
        initial_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(initial_updated_at, self.model.updated_at)

    def test_to_dict(self):
        model1_dict = self.model.to_dict()
        self.assertEqual(self.model.__class__.__name__, "BaseModel")
        self.assertIsInstance(model1_dict["created_at"], str)
        self.assertIsInstance(model1_dict["updated_at"], str)

if __name__ == "__main__":
    unittest.main()
