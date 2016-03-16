import os
import sys
import dxpy
import logging
import json


logger = logging.getLogger(__name__)
logger.addHandler(dxpy.DXLogHandler())
logger.propagate = False
logger.setLevel('INFO')


def load_json_from_file(path_to_file):

    """Load JSON file from a file

    :param: `path_to_file`: Full path to a file to convert to JSON object
    :returns: The input file as a serialized JSON object
    """

    json_object = {}
    with open(path_to_file, 'r') as file_data:
        json_object = json.load(file_data)

    return json_object
