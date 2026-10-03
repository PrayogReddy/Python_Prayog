import subprocess

# subprocess.run("echo Hello world", shell=True, check=True)
# subprocess.run(["echo", "Hello world"], check=False)

# subprocess.run("dir", shell=True, check=False)
# subprocess.run("mkdir demo_folder", shell=True, check=False)
# subprocess.run("echo Finished!!!", shell=True, check=False)
# subprocess.run("dir", shell=True, check=False)

# res = subprocess.run("echo Hello World", capture_output=True, text=True, shell=True, check=False)
# print(res.stdout)

# res = subprocess.run("Hello", capture_output=True, text=True, shell=True, check=False)
# print("Result out: ", res.stdout)
# print("Result Err: ", res.stderr)

# res = subprocess.run("ping google.com", shell=True, check=False)
# print("return code:",res.returncode)

# res = subprocess.run("ping ksdhfkhfidgoogle.com", shell=True, check=False)
# print("return code:",res.returncode)

# subprocess.run("echo Hello && echo World!", shell=True, check=False)

cmd = ( 
    "echo creating a folder &&"
    "mkdir demo_folder1 &&"
    "cd demo_folder1 &&"
    "echo creating a file inside the folder > info.txt &&"
    "dir"
)
subprocess.run(cmd, shell=True, check=False)
