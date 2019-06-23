"""Module for json file parsing."""
# global imports
import json

# local imports
import base


def _byteify(data, ignore_dicts=False):
    """Convert data into byteified value/string representation."""
    if isinstance(data, unicode):
        return data.encode('utf-8')
    if isinstance(data, list):
        return [_byteify(item, ignore_dicts=True) for item in data]
    if isinstance(data, dict) and not ignore_dicts:
        return {
            _byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True)
            for key, value in data.iteritems()
        }
    return data


class jsonParser(base.Parser):
    """Class for parsing jsonfiles.

    Args:
        filepath (str): path of file to parse.
    """
    def _process_file(self):
        """Process filepath into usable data."""
        with open(self._filepath) as json_file:
            self._user_collection = _byteify(
                json.load(json_file, object_hook=_byteify),
                ignore_dicts=True
            )
