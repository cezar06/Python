import os
def write_files(dir_path, file_path):
    files = []
    for f in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, f)):
            if f[0] == 'A':
                files.append(os.path.join(dir_path, f))
    with open(file_path, 'w') as f:
        for file in files:
            f.write(file + '')
    return files
write_files(r"C:\Users\Cezar\Desktop\python\lab4", r"C:\Users\Cezar\Desktop\python\lab4\file.txt")