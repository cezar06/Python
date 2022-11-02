import os
def search(target, to_search, callback):
    if os.path.isfile(target):
        with open(target, 'r') as f:
            if to_search in f.read():
                return [target]
    elif os.path.isdir(target):
        files = []
        for root, dirs, files in os.walk(target):
            for f in files:
                try:
                    with open(os.path.join(root, f), 'r') as f:
                        if to_search in f.read():
                            files.append(os.path.join(root, f))
                except Exception as e:
                    callback(e)
        return files
    else:
        raise ValueError('Target must be a file or a directory')


print(search(r"C:\Users\Cezar\Desktop\python\lab4\file.txt", 'Cezar', print))
print(search(r"C:\Users\Cezar\Desktop\python\lab4", 'a', print))