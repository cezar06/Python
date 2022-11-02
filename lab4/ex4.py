import os
import sys
def list_extensions(path):
    exts = []
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            ext = os.path.splitext(f)[1]
            if ext not in exts:
                exts.append(ext)
    return sorted(exts)

def main():
    print(list_extensions(sys.argv[1]))

if __name__ == '__main__':
    main()

#py C:\Users\Cezar\Desktop\python\lab4\ex4.py C:\Users\Cezar\Desktop\python\lab4\