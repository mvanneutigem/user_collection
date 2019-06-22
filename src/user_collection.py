"""Module containing user collection class."""
# global imports
import logging
import os

# local imports
import user_collection_parser

LOGGER = logging.getLogger(__name__)

class UserCollection(object):
    """Class for interacting with user data.
    
    Args:
        filepath (str): path to file to populate class from.
    """
    # overrides
    def __init__(self, filepath=None):
        self._filepath = filepath
        self._users = []
        if self._filepath:
            self._populate()
        
    def __iter__(self):
        """Allow class to be accessed as an iterator."""
        for user in self._users:
            yield user
        
    def __getitem__(self, key):
        """Allow class to be accessed by key.
        
        Args:
            key (int): index of user data to return.
        """
        return self._users[key]
    
    # public methods:
    def add_user(self, name, phone, address):
        """Add user to user collection.
        
        Args:
            name (str): Full name of user to add.
            phone (str): Phone number of user to add.
            address dict(str: str): Address of user to add.
        """
        user = {
            "Name": name,
            "Phone": phone,
            "Address": address
        }
        self._users.append(user)
        
    def remove_user_by_index(self, index):
        """Remove user at given index.
        
        Args:
            index (int): index of user to remove.
        """
        self._users.pop(index)
        
    def clear(self):
        """Clear current data in class."""
        self._users = []
    
    def get_supported_formats(self):
        """Utility function to query supported formats.
        
        Returns:
            (list): list of supported file extensions.
        """
        return user_collection_parser.SUPPORTED_EXTENSIONS
    
    # private methods
    def _populate(self):
        """Populate class by parsing filepath."""
        extension = os.path.splitext(self._filepath)[1].replace('.','')
        if extension in user_collection_parser.SUPPORTED_EXTENSIONS:
            Parser = getattr(
                user_collection_parser, "{0}Parser".format(extension)
            )
            parser_object = Parser(self._filepath)
            self._users = parser_object.as_list().get("Users")
        else:
            LOGGER.warn('Extension not supported! {0}'.format(extension))
    
    # properties
    @property    
    def users(self):
        """users attribute"""
        return self._users
    
    @users.setter
    def users(self, value):
        if isinstance(value, list):
            self._users = value
        else:
            LOGGER.warn(
                "Failed to set attribute users has to be of type list."
            )