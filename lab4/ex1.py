import os
def list_extensions(path):
    exts = []
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            ext = os.path.splitext(f)[1]
            if ext not in exts:
                exts.append(ext)
    return sorted(exts)

print(list_extensions(r"C:\Users\Cezar\Desktop\python\lab4"))