import os
import sys
import dxpy
import logging
import json


logger = logging.getLogger(__name__)
logger.addHandler(dxpy.DXLogHandler())
logger.propagate = False
logger.setLevel("INFO")


def load_json_from_file(path_to_file):

    """Load JSON file from a file

    :param: `path_to_file`: Full path to a file to convert to JSON object
    :returns: The input file as a serialized JSON object
    """

    json_object = {}
    with open(path_to_file, "r") as file_data:
        json_object = json.load(file_data)

    return json_object


def check_compression(filename):

    """Identify the compression used for file

    :param: `filename`: The filename to check for compression
    :returns: The suffix of a file (if compressed by gzip or bzip2)
    """

    if filename.endswith(".bz2"):
        return ".bz2"
    elif  filename.endswith(".gz"):
        return ".gz"
    else:
        return ""



def get_file_metadata(filename):

    """Retrieve the filename metadata

    :param: `filename`: The filename to extract filename metadata from
    :returns: Object with sampleID and chr
    """

    basename_ = os.path.basename(str(fname)).split(".")
    try:
    	return { "sampleID": basename_[0], "chr": basename_[1] }
    except:
    	return { "sampleID": basename_[0], "chr": None }
