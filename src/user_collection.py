"""Module containing user collection class."""
# global imports
import logging
import os

# local imports
import user_collection_parser

LOGGER = logging.getLogger(__name__)
SUPPORTED_EXTENSIONS = ["json", "xml"]

class UserCollection(object):
    """Class for interacting with user data.
    
    Args:
        filepath (str): path to file to populate class from.
    """
    # overrides
    def __init__(self, filepath=None):
        print "init class."
        self._filepath = filepath
        if self._filepath:
            self._populate()
        
    def __iter__(self):
        """Allow class to be accessed as an iterator."""
        
    def __getitem__(self):
        """Allow class to be accessed by key."""
    
    # methods
    def _populate(self):
        """Populate class by parsing filepath."""
        extension = os.path.splitext(self._filepath)
        if extension in SUPPORTED_EXTENSIONS:
            Parser = getattr(parser, "{0}Parser".format(extension))
            parser_object = Parser(self._filepath)
            self._users = parser_object.as_list()
    
    # properties
    @property    
    def users(self):
        """users attribute"""
        return self._users
    
    def users(self, value):
        if isinstance(value, list):
            self._users = value
        else:
            LOGGER.warn(
                "Failed to set attribute users has to be of type list."
            )