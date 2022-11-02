import os
def get_file_info(path):
    if os.path.isfile(path):
        return {'full_path': os.path.abspath(path), 
        'file_size': os.path.getsize(path), 
        'file_extension': os.path.splitext(path)[1], 
        'can_read': os.access(path, os.R_OK), 
        'can_write': os.access(path, os.W_OK)}

print(get_file_info(r"C:\Users\Cezar\Desktop\python\lab4\file.txt"))