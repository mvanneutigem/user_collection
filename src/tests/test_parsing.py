"""Module for testing parsing operations."""
# global imports
import unittest
import os

# local imports
from ..user_collection import UserCollection


class TestParsing(unittest.TestCase):
    """Unittest class for testing parsing."""
    def test_parse_xml(self):
        """Unittest for xml parsing."""
        filepath = "resources/xml_data.xml"
        directory = os.path.dirname(os.path.realpath(__file__))
        os.path.join(directory, filepath)
        user_object = UserCollection(filepath)

        # expected data
        user_zero = {
            "Name": "Howard Snyder",
            "Phone": "(503) 555-7555",
            "Address": {
                    "Address": "2732 Baker Blvd.",
                    "City": "Eugene",
                    "Region": "OR",
                    "PostalCode": "97403",
                    "Country": "USA"
                }
        }

        user_three = {
            "Name": "Jaime Yorres",
            "Phone": "(415) 555-5938",
            "Address": {
                    "Address": "87 Polk St. Suite 5",
                    "City": "San Francisco",
                    "Region": "CA",
                    "PostalCode": "94117",
                    "Country": "USA"
                }
        }

        self.assertDictEqual(user_object[0], user_zero)
        self.assertDictEqual(user_object.users[3], user_three)

    def test_parse_json(self):
        """Unittest for json parsing."""
        filepath = "resources/json_data.json"
        directory = os.path.dirname(os.path.realpath(__file__))
        os.path.join(directory, filepath)
        user_object = UserCollection(filepath)

        # expected data
        user_zero = {
            "Name": "Lars Hamon",
            "Phone": "(02) 7432 7401",
            "Address": {
                    "Address": "Ap #345-9065 Donec St.",
                    "City": "Huntsville",
                    "Region": "AL",
                    "PostalCode": "221017",
                    "Country": "Anguilla"
                }
        }

        user_two = {
            "Name": "Marvin Romero",
            "Phone": "(05) 1557 2801",
            "Address": {
                    "Address": "P.O. Box 441, 7141 Sodales Street",
                    "City": "Maringa",
                    "Region": "PR",
                    "PostalCode": "68938",
                    "Country": "Australia"
                }
        }

        self.assertDictEqual(user_object[0], user_zero)
        self.assertDictEqual(user_object.users[2], user_two)
