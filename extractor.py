import os
import shutil

def rename(path,addt):
    split = list(os.path.splitext(path))
    split[0] += addt
    joined = "".join(split)
    return joined

files = os.listdir('.')
folders = []
try:
    os.rmdir("# Compiled")
    os.rmdir("# Duplicates")
except:
    print("Default folders not generated, generating now")
os.mkdir("# Compiled")
os.mkdir("# Duplicates")
exit()
compiled = os.path.join(os.getcwd(), "# Compiled")
dups = os.path.join(os.getcwd(), "# Duplicates")

for item in files:
    if os.path.isdir(item) and item != "# Compiled" and item != "# Duplicates":
        folders.append(item)


print(folders)


for folder in folders:

    currentDirectory = os.path.join(os.getcwd(), folder)
    items = os.listdir(currentDirectory)

    for item in items:

        itemPath = os.path.join(currentDirectory, item)
        dest = os.path.join(compiled, folder+" " +item)
        
        print(itemPath)

        if item in os.listdir(compiled):
            shutil.copy(os.path.join(compiled, item), os.path.join(dups,rename(item, " (1)")))
            shutil.copy(itemPath, os.path.join(dups,rename(item, " (2)")))
            print("Duplicate found, fix names")
        

        try:
            # copy file
            shutil.copy(itemPath, dest)
            # destination folder after copying
        except SameFileError:
            print("We are trying to copy the same File")
        except IsADirectoryError:
            print("The destination is a directory")