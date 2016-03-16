import os
import sys
import dxpy
import logging
import math
from dx_applet_utilities.manage_command_execution import execute_command, check_execution_syscode
from multiprocessing import cpu_count


logger = logging.getLogger(__name__)
logger.addHandler(dxpy.DXLogHandler())
logger.propagate = False
logger.setLevel('INFO')


def max_memory(percent_to_utilize):

    """Return the max RAM to be used by applet

    :param: `percent_to_utilize`: Percent of RAM to allocate for processes
    :returns: The amount of RAM in MB to allocate to a given process
    """

    total_ram_cmd = "head -n1 /proc/meminfo"
    calculate_ram_cmd = "awk '\{ print int($2*{0}/1024) \}'".format(percent_to_utilize)
    ram_allocation = execute_command("{0} | {1}".format(
        total_ram_cmd, calculate_ram_cmd)
    )

    if ram_allocation["sysCode"] == 0:
        return int(ram_allocation["out"])
    else:
        logger.warning("{0}: Unable to calculate RAM usage! Setting to default".format(
            strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        )
        return 512


def number_of_cpus(percentage=1):
    
    """Return the number of CPUs on running instance

    :param: `percentage`: Percent of CPUs to allocate for multithreaded processes
    :returns: The number of CPUs to be used
    """

    return int(cpu_count()*percentage)
