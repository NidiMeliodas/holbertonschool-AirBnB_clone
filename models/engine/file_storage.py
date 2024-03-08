#!/usr/bin/python3
#!/usr/bin/python3
"""Module for Base Model unittests."""
import unittest
from unittest.mock import patch
from io import StringIO
import datetime

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests Base Model class."""

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, expected_output, mock_stdout):
        """Assert stdout."""
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_save(self):
        """Test save()"""
        my_model = BaseModel()
        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    @patch('builtins.open', create=True)
    def test_save2(self, mock_open):
        my_model = BaseModel()
        my_model.save()
        expected = "BaseModel." + my_model.id
        mock_open.return_value.__enter__.return_value.read.return_value = ""
        with open("file.json", "r") as f:
            self.assertIn(expected, f.read())

    def test_to_dict(self):
        """Test to_dict()"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.number = 89
        my_model_json = my_model.to_dict()
        self.assertEqual(my_model_json["id"], my_model.id)
        self.assertEqual(my_model_json["created_at"],
                         my_model.created_at.isoformat())

    def test__str__(self):
        """Test __str__()"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.number = 89
        expected_output = f"[BaseModel] ({my_model.id}) {my_model.__dict__}\n"
        self.assert_stdout(expected_output, str(my_model))

    def test_init(self):
        """Test __init__()"""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime.datetime)
        self.assertIsInstance(my_model.updated_at, datetime.datetime)


if __name__ == "__main__":
    unittest.main()
