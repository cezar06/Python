import os
import re

def search_files(directory, regex):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if re.search(regex, file) or re.search(regex, open(os.path.join(root, file)).read()): 
                if re.search(regex, file) and re.search(regex, open(os.path.join(root, file)).read()):
                    print(">>", os.path.join(root, file))
                else:
                    print(os.path.join(root, file))

search_files(".", r'\d+')


