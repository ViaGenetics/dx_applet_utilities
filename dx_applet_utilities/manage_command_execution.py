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


def check_execution_syscode(command_result, command_description):

    """Verifies if executed command finished successfully

    :param: `command_result`: Object returned from execute_command function
    :param: `command_description`: Description of command for display in logs
    """

    if command_result["sysCode"] == 0:
        logger.info('{0}: Execution of {1} finished successfully!'.format(
            strftime("%Y-%m-%d %H:%M:%S", gmtime()), command_description)
        )

    else:
        logger.error('{0}: Execution of {1} failed!'.format(
            strftime("%Y-%m-%d %H:%M:%S", gmtime()), command_description)
        )
        logger.error('{0}: Command that was executed: {1}'.format(
            strftime("%Y-%m-%d %H:%M:%S", gmtime()), command_result["cmd"])
        )
        logger.error('STDOUT: {0}'.format(command_result["out"]))
        logger.error('STDERR: {0}'.format(command_result["err"]))
        sys.exit(1)
