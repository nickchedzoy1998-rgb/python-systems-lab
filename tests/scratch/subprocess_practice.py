import subprocess
import sys

"""
result = subprocess.run(
    [path_to_python_executable, run_code_flag, python_code_string], # <-- whole list = full command + its arguments as separate strings
    optional_settings=True_or_False,
)
"""

# path_to_python_executable: The file path on your computer to the python (or python3) program currently running your script
    # sys.executable makes new process use same Python interpreter already in.
# run_code_flag: Command that Python reads
    # "-c" = Take next argument and run - no requirement to find .py file
# python_code_string: Actual Python code to run, as a string.

result = subprocess.run(
    [sys.executable, "-c", "import sys; print('Hello from subprocess', file=sys.stderr); raise SystemExit(1)"],
    capture_output=True,
    text=True,
)

print(result.stderr)
print(result.returncode)
