"""Module for xml file parsing."""
# global imports
from xml.etree import ElementTree

# local imports
import base


class xmlList(list):
    """Utility class to convert xml to python list.

    Args:
        root (element): parent element to iterate over.
    """
    def __init__(self, root):
        for element in root:
            if len(element):
                if len(element) == 1 or element[0].tag != element[1].tag:
                    self.append(xmlDict(element))
                elif element[0].tag == element[1].tag:
                    self.append(xmlList(element))
            elif element.text:
                text = element.text.strip()
                if text:
                    self.append(text)


class xmlDict(dict):
    """Utility class to convert xml to python dict.

    Args:
        root (element): parent element to iterate over.
    """
    def __init__(self, root):
        if root.items():
            self.update(dict(root.items()))
        for element in root:
            if len(element):
                # treat as dict
                if len(element) == 1 or element[0].tag != element[1].tag:
                    update_dict = xmlDict(element)
                # treat as list
                else:
                    update_dict = xmlList(element)

                if element.items():
                    update_dict.update(dict(element.items()))
                self.update({element.tag: update_dict})

            elif element.items():
                self.update({element.tag: dict(element.items())})

            else:
                self.update({element.tag: element.text})


class xmlParser(base.Parser):
    """Class for parsing xmlfiles.

    Args:
        filepath (str): path of file to parse.
    """
    def _process_file(self):
        """Process filepath into usable data."""
        tree = ElementTree.parse(self._filepath)
        root = tree.getroot()
        self._user_collection = xmlDict(root)
