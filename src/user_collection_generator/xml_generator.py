"""Module for xml file generating."""
# global imports
from xml.etree import ElementTree

# local imports
import base


def _data_to_xml(data, name='Root'):
    """Convert given data to xml format.

    Args:
        data (dict): data to convert to xml.
    """
    root = ElementTree.Element(name)
    return ElementTree.tostring(_build_xml(root, data))


def _build_xml(root, data):
    """Build an data into given root.

    Args:
        root (xml.etree.ElementTree.element): top element of the xml data.
        data (dict | list | tuple | string): data to add to root.
    """
    if isinstance(data, dict):
        for key, value in data.iteritems():
            sub_element = ElementTree.SubElement(root, key)
            _build_xml(sub_element, value)
    elif isinstance(data, tuple) or isinstance(data, list):
        for value in data:
            sub_element = ElementTree.SubElement(root, 'User')
            _build_xml(sub_element, value)
    elif isinstance(data, basestring):
        root.text = data
    else:
        root.text = str(data)
    return root


class xmlGenerator(base.Generator):
    """Class for parsing xmlfiles.

    Args:
        data (dict): data to write out to file.
        filepath (str): path of file to generate.
    """
    def _process_to_file(self):
        """Process filepath into usable data."""
        xml_data = _data_to_xml(self._data)
        with open(self._filepath, 'w') as xml_file:
            xml_file.write(xml_data)
        return self._filepath
