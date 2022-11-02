import os
def search(target, to_search):
    if os.path.isfile(target):
        with open(target, 'r') as f:
            if to_search in f.read():
                return [target]
    elif os.path.isdir(target):
        files = []
        for root, dirs, files in os.walk(target):
            for f in files:
                with open(os.path.join(root, f), 'r') as file:
                    if to_search in file.read():
                        files.append(os.path.join(root, f))
        return files
    else:
        raise ValueError('Target must be a file or a directory')

print(search(r"C:\Users\Cezar\Desktop\python\lab4\file.txt", 'Cezar'))
print(search(r"C:\Users\Cezar\Desktop\python\lab4", 'a'))