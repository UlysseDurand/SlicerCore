# Baseline Slicer repository, change this when rebasing
GIT_URL = "https://github.com/UlysseDurand/Slicer/"
GIT_REVISION = "00876fac230dfad249179f28e1bfb33526a7b7ab"

# Directories used by the scripts
SLICER_DIR = "Slicer"
PATCH_DIR = "patch"
VTK_WHEEL = "/home/ulysse-durand/Downloads/artifacts/build/dist/vtk-9.7.20260627.dev0+mr96942-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.whl"
VTK_SDK_WHEEL = "/home/ulysse-durand/Downloads/artifacts/build/wheel_sdks/vtk_sdk-9.7.20260627.dev0-cp314-cp314-linux_x86_64.whl"

import subprocess
import os

def execute_process(cmd: str, cwd: str = ".") -> str:
    """Run a shell command and return the process standard output as a str.
    Throws an exception with subprocess stderr if return code is not zero.
    """
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error running command: {cmd}\nError message:\n{e.stderr}\n")


def mkpath(file_path: str) -> None:
    """Create the directories tree for given file path"""
    directory = os.path.dirname(file_path)
    if directory:
        os.makedirs(directory, exist_ok=True)

