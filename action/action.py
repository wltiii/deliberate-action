import os
import subprocess



origWD = os.getcwd()
print(origWD)

msg = "repo.py runs repo commands"
print(msg)

result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print("return code is:")
print(result.returncode)
print('stdout is:')
print(result.stdout)
print('stderr is:')
print(result.stderr)

msg = "changing directory"
print(msg)

os.chdir("/home/worldwidewilly/workspace/workman")
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
# print("return code is:")
print(f'return code is: {result.returncode}.')
# print(result.returncode)
print(f'stdout is: {result.stdout}.')
# print(result.stdout)
print(f'stderr is: {result.stderr if result.stderr else ""}.')
# print(result.stderr)

msg = "reverting to original directory"
print(msg)

os.chdir(origWD)
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print("return code is:")
print(result.returncode)
print('stdout is:')
print(result.stdout)
print('stderr is:')
print(result.stderr)

# print("checking navigation")
# result = subprocess.run(["cd", "/home/worldwidewilly/workspace"], capture_output=True, text=True)
# print("return code is:")
# print(result.returncode)
# print('stdout is:')
# print(result.stdout)
# print('stderr is:')
# print(result.stderr)

# result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
# print("return code is:")
# print(result.returncode)
# print('stdout is:')
# print(result.stdout)
# print('stderr is:')
# print(result.stderr)
