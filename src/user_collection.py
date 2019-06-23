"""Module containing user collection class."""
# global imports
import logging
import os
import pprint
import tempfile
import webbrowser
from xml.etree import ElementTree

# local imports
import user_collection_parser
import user_collection_generator

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

    def to_file(self, filepath):
        """Write out current class data to file.

        Args:
            filepath (str): path to file to write class data to.
        """
        extension = os.path.splitext(filepath)[1].replace('.', '')
        if extension in user_collection_parser.SUPPORTED_EXTENSIONS:
            Generator = getattr(
                user_collection_generator, "{0}Generator".format(extension)
            )
            generator_object = Generator({"Users": self.users}, filepath)
            self._filepath = generator_object.run()
        else:
            LOGGER.warn(
                'Generator Extension not supported! {0}'.format(extension)
            )

    def output_to_terminal(self, format="text"):
        """Convenience function to display data to user.

        Args:
            format (str): name of format to output in (text or html)
        """
        if format == "text":
            pprint.pprint(self._users, depth=3)
        elif format == "html":
            self._to_html()
        else:
            LOGGER.warn(
                'Output format not supported! {0}'.format(format)
            )

    # private methods
    def _to_html(self):
        """Convert internal data to html format and open with standard app."""
        html = ElementTree.Element('html')
        body = ElementTree.Element('body')
        html.append(body)

        table = ElementTree.Element('table')
        body.append(table)
        tr = ElementTree.Element('tr')
        table.append(tr)
        for heading in ["Name", "Phone", "Address"]:
            th = ElementTree.Element('th')
            tr.append(th)
            th.text = heading

        # iterate self for data.
        for user in self:
            tr = ElementTree.Element('tr')
            table.append(tr)

            for label in ["Name", "Phone"]:
                td = ElementTree.Element('td')
                tr.append(td)
                td.text = user.get(label)

            td = ElementTree.Element('td')
            tr.append(td)
            td.text = user.get("Address").get("Address")
            for field in ["City", "Region", "PostalCode", "Country"]:
                td.text += ", {0}".format(user.get("Address").get(field))

        # save html to temp file.
        _, path = tempfile.mkstemp(".html", "tmp_")
        url = 'file://' + path

        ElementTree.ElementTree(html).write(
            path,
            encoding='utf-8',
            method='html'
        )

        webbrowser.open(url)

    def _populate(self):
        """Populate class by parsing filepath."""
        extension = os.path.splitext(self._filepath)[1].replace('.', '')
        if extension in user_collection_parser.SUPPORTED_EXTENSIONS:
            Parser = getattr(
                user_collection_parser, "{0}Parser".format(extension)
            )
            parser_object = Parser(self._filepath)
            self._users = parser_object.as_list().get("Users")
        else:
            LOGGER.warn(
                'Parser Extension not supported! {0}'.format(extension)
            )

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
