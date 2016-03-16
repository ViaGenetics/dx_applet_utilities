import os
import sys
import dxpy
import logging
import math


logger = logging.getLogger(__name__)
logger.addHandler(dxpy.DXLogHandler())
logger.propagate = False
logger.setLevel("INFO")


def number_of_files_per_node(files, number_of_nodes):

    """Determines the number of files each node will process in scatter gather environment

    :param: `files`: Array of files to be processed
    :param: `number_of_nodes`: Number of nodes desired for scatter gather
    :returns: The number of files to be processed per node
    """

    files_per_node = float(len(files))/float(number_of_nodes)
    if files_per_node > 0.:
        return int(math.floor(files_per_node))
    else:
        return int(math.ceil(files_per_node))
