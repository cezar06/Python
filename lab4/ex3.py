import os
def get_last_20(path):
    if os.path.isfile(path):
        with open(path, 'r') as f:
            return f.read()[-20:]
    elif os.path.isdir(path):
        exts = {}
        for root, dirs, files in os.walk(path):
            for f in files:
                ext = os.path.splitext(f)[1]
                if ext not in exts:
                    exts[ext] = 1
                else:
                    exts[ext] += 1
        return sorted(exts.items(), key=lambda x: x[1], reverse=True)
    else:
        return None
    
print(get_last_20(r"C:\Users\Cezar\Desktop\python\lab4\file.txt"))
print(get_last_20(r"C:\Users\Cezar\Desktop\python\lab4"))