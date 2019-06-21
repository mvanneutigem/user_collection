"""Module for json file parsing."""
# global imports
import json

# local imports
import base

class jsonParser(base.Parser):
    """Class for parsing jsonfiles.
    
    Args:
        filepath (str): path of file to parse.
    """
    def _process_file(self):
        """Process filepath into usable data."""
        