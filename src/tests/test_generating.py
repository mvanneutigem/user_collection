"""Module for testing generation operations."""
# global imports
import unittest
import os

# local imports
from ..user_collection import UserCollection


class TestGenerating(unittest.TestCase):
    """Unittest class for testing generating."""
    def test_generate(self):
        """Unittest for xml and json generating."""
        for filepath in [
            "resources/xml_output.xml",
            "resources/json_output.json"
        ]:
            directory = os.path.dirname(os.path.realpath(__file__))
            os.path.join(directory, filepath)
            user_object = UserCollection()

            address = {
                "Address": "2732 Baker Blvd.",
                "City": "Eugene",
                "Region": "OR",
                "PostalCode": "97403",
                "Country": "USA"
            }
            user_object.add_user(
                "Howard Snyder",
                "(503) 555-7555",
                address
            )
            address = {
                "Address": "P.O. Box 441, 7141 Sodales Street",
                "City": "Maringa",
                "Region": "PR",
                "PostalCode": "68938",
                "Country": "Australia"
            }
            user_object.add_user(
                "Marvin Romero",
                "(05) 1557 2801",
                address
            )

            user_object.to_file(filepath)
            parsed_user_object = UserCollection(filepath)

            self.assertDictEqual(user_object[0], parsed_user_object.users[0])
            self.assertDictEqual(user_object.users[1], parsed_user_object[1])
