import os
import sys
import dxpy
import logging
import subprocess


logger = logging.getLogger(__name__)
logger.addHandler(dxpy.DXLogHandler())
logger.propagate = False
logger.setLevel('INFO')


def execute_command(command, debug=False):

    """Executes given command

    :param: `command`: Command to execute
    :param: `debug`: If True, will log all messages to console
    :returns: Object with results of the executed command
    """

    if debug:
        p = subprocess.Popen(command, shell=True)
        p.wait()
        out = ""
        err = ""
        sys_code = p.returncode
    else:
        p = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        out,err = p.communicate()
        sys_code = p.returncode

    return {
            "sysCode": sys_code,
            "cmd": command,
            "out": out.strip(),
            "err": err.strip()
    }
