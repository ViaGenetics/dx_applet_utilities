import os
import sys
import dxpy
import logging
import math


logger = logging.getLogger(__name__)
logger.addHandler(dxpy.DXLogHandler())
logger.propagate = False
logger.setLevel('INFO')
