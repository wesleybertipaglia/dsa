from os import listdir
from os.path import isfile, join
from collections import deque

def print_files_names(start_dir):
    search_queue = deque()
    search_queue.append(start_dir)
    while search_queue:
        dir = search_queue.popleft()
        files = listdir(dir)
        for file in sorted(files):
            fullpath = join(dir, file)
            if isfile(fullpath):
                print(file)
            else:
                search_queue.append(fullpath)
    return False
        
def test():
    print_files_names("pics")

test()