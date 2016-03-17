import os
import sys
import dxpy
import logging
import math
import operator


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


def distribute_files_by_size(file_sizes, dx_file_objects, number_of_nodes):

    """Organizes all files to be distributed across all nodes of scatter gather
    equally based on total file size to process

    :param: `file_sizes`: Array of file sizes to be processed
    :param: `dx_file_objects`: dxpy object of file objects
    :param: `number_of_nodes`: Number of nodes desired for scatter gather
    :returns: Object that organizes file by size to be distributed across nodes
    """

    files_per_node = number_of_files_per_node(file_sizes, number_of_nodes)
    sorted_file_sizes = sorted(file_sizes.items(), key=operator.itemgetter(1))

    job_idx = 1
    jobs_object = {}

    for file_name, file_size in sorted_file_sizes:
        if job_idx > number_of_nodes:
            job_idx = 1

        try:
            jobs_object[job_idx].append(dx_file_objects[file_name])
        except KeyError:
            jobs_object[job_idx] = [dx_file_objects[file_name]]

        job_idx += 1

    return jobs_object
