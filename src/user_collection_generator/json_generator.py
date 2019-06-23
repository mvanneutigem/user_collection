"""Module for json file generating."""
# global imports
import json

# local imports
import base


class jsonGenerator(base.Generator):
    """Class for generating jsonfiles.

    Args:
        data (dict): data to write out to file.
        filepath (str): path of file to generate.
    """
    def _process_to_file(self):
        """Process data into json file."""
        with open(self._filepath, 'w') as json_file:
            json.dump(self._data, json_file, indent=4)
        return self._filepath
