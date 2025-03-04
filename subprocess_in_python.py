#running a simple shell command
import subprocess

#list all files in a directory
"""
#for linux
result = subprocess.run(['ls', '-l'], shell=True,
                        capture_output=True, text=True)
print(result.stdout)

#for windows
result = subprocess.run(['dir'], shell=True,
                        capture_output=True, text=True)
print(result.stdout)
"""

#checking disk space
"""
#for linux
result = subprocess.run(['df', '-h'], shell=True,
                        capture_output=True, text=True)
print(result.stdout)

#for windows
result = subprocess.run(['tasklist'], shell=True,
                        capture_output=True, text=True)
print(result.stdout)
"""

#running an external program
#linux
server = "google.com"
result = subprocess.run(["ping", "-c", "4", server],
                        capture_output=True, text=True)

if result.returncode == 0:
    print("Server is reachable")
    print(result.stdout)
else:
    print("Server is unreachable")
    print(result.stderr)

#windows
server = "google.com"
result = subprocess.run(["ping", "-n", "4", server],
                        capture_output=True, text=True)

if result.returncode == 0:
    print("Server is reachable")
    print(result.stdout)
else:
    print("Server is unreachable")
    print(result.stderr)
