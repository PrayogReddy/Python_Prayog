## CLI commands for managing Python packages using pip:
# pip install package_name
# pip uninstall package_name
# pip list
# pip show package_name
# pip freeze > requirements.txt
# pip install -r requirements.txt

## CLI commands for managing virtual environments using venv:
# python -m venv myenv
# myenv\Scripts\activate (windows)
# source myenv/bin/activate (linux/mac)
# deactivate

import os

# print(os.getcwd())

# os.chdir("C:\\Users\\prayo\\Python")
# print(os.getcwd())

# print(os.listdir())

# os.mkdir("demo_folder")

# os.makedirs("parent/child")

# os.rmdir("demo_folder")

# os.removedirs("parent/child")

# os.rename("log.txt", "log1.txt")

# print(os.path.exists("log1.txt"))

# print(os.path.getsize("log1.txt"))

# if not os.path.exists("logs"):
#     os.mkdir("logs")
# with open("logs/logs1.txt", "w") as file:
#     file.write("Sample log data")

# os.rename("logs/logs1.txt", "logs/logs_new.txt")

# for file in os.listdir("logs"):
#     print(file)