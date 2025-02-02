import sys

# The `sys` module provides access to some variables used or maintained by the interpreter
# and to functions that interact strongly with the interpreter.

# Example: Getting the list of command line arguments
# `sys.argv` is a list in Python, which contains the command-line arguments passed to the script.
print("Command Line Arguments:", sys.argv)

# Example: Exiting the program
# `sys.exit()` allows you to exit from Python. The optional argument can be an integer giving the exit status.
# `sys.exit(0)` indicates a successful termination.
# `sys.exit(1)` or any other non-zero value indicates an abnormal termination.
# sys.exit(0)

# Example: Getting the Python version
# `sys.version` returns a string containing the version number of the Python interpreter plus additional information.
print("Python Version:", sys.version)

# Example: Getting the platform
# `sys.platform` returns a string that identifies the platform on which Python is running.
print("Platform:", sys.platform)

# Example: Getting the path of the Python interpreter
# `sys.executable` returns the absolute path of the Python interpreter binary.
print("Python Executable Path:", sys.executable)

# Example: Getting the list of module search paths
# `sys.path` is a list of strings that specifies the search path for modules.
print("Module Search Paths:", sys.path)

# Example: Getting the standard input, output, and error streams
# `sys.stdin`, `sys.stdout`, and `sys.stderr` are file objects corresponding to the interpreter’s standard input, output, and error streams.
print("Standard Input:", sys.stdin)
print("Standard Output:", sys.stdout)
print("Standard Error:", sys.stderr)

####################################################################################################

import subprocess

# Example: Running a simple command
result = subprocess.run(['powershell', '-Command', 'Get-ChildItem'], capture_output=True, text=True)
print("Output:", result.stdout)
