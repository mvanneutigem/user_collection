"""Module containing class for parsing files."""


class Parser(object):
    """Base class for parsing files.

    To add support for a new file type;
        - inherit from this class.
        - implement the _process_file method to fill self._user_collection
            with data where the first key == Users.
        - add an import to thew new parser in the user_collection_parser init.

    Args:
        filepath (str): path of file to parse.
    """
    def __init__(self, filepath):
        self._filepath = filepath
        self._user_collection = {}
        self._process_file()

    def _process_file(self):
        """Process filepath into usable data."""
        raise NotImplementedError

    def as_list(self):
        """Return parsed data as list of users.

        Returns:
            (list): list of users containing parsed data.
        """
        return self._user_collection
