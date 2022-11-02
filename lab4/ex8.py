import os
def list_files(dir_path):
    files = []
    for f in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, f)):
            files.append(os.path.join(dir_path, f))
    return files

print(list_files(r"C:\Users\Cezar\Desktop\python\lab4"))