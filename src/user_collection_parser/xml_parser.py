"""Module for xml file parsing."""
# global imports
import cElementTree as ElementTree

# local imports
import base

class xmlParser(base.Parser):
    """Class for parsing xmlfiles.
    
    Args:
        filepath (str): path of file to parse.
    """
    def _process_file(self):
        """Process filepath into usable data."""
        tree = ElementTree.parse(filepath)
        root = tree.getroot()
        for element in root:
            print element