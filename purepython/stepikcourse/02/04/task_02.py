import os
import os.path


def isExistsPythonFiles(files):
    for f in files:
        if f.count(".py") > 0:
            return True
    return False


os.getcwd()
os.chdir("_")

mass = []
for current_dir, dirs, files in os.walk("main"):
    if isExistsPythonFiles(files):
        mass.append(current_dir.replace("\\","/"))

for i in sorted(mass):
    print(i)

