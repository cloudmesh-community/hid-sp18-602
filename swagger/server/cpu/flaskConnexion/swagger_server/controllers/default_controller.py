import connexion
import six
import os, platform, subprocess, re

from swagger_server.models.cpu import CPU  # noqa: E501
from swagger_server import util

def cpu_get():  # noqa: E501
    os_info =""
    """cpu_get

    Returns CPU information from host server # noqa: E501

    :rtype: CPU
    """
    if platform.system() == "Windows":
        os_info = platform.processor()
    elif platform.system() == "Darwin":
        command = "/usr/sbin/sysctl -n machdep.cpu.brand_string"
        os_info = subprocess.check_output(command, shell=True).strip()
    elif platform.system() == "Linux":
        command = "cat /proc/cpuinfo"
        all_info = subprocess.check_output(command, shell=True).strip()
        for line in all_info.split("\n"):
            if "model name" in line:
                os_info = re.sub(".*model name.*:", "", line, 1)

    return CPU(os_info)
