"""Module containing class for generating files."""


class Generator(object):
    """Base class for generating files.

    To add support for a new file type;
    - inherit from this class.
    - implement the _process_to_file method to write data to filepath.
    - add import to thew new generator in the user_collection_generator init.

    Args:
        data (dict): data to write out to file.
        filepath (str): path of file to generate.
    """
    def __init__(self, data, filepath):
        self._filepath = filepath
        self._data = data

    def _process_to_file(self):
        """Process data into file."""
        raise NotImplementedError

    def run(self):
        """Generate file.

        Returns:
            (str): path to generated file.
        """
        return self._process_to_file()
