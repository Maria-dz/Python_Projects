import os.path
import tempfile
import random


class File:
    def __init__(self, path):
        if not os.path.exists(path):
            with open(path, 'w') as f:
                f.write('')
        self.path = path

    def read(self):
        with open(self.path, 'r') as f:
            st = f.read()
        return st

    def write(self, string):
        with open(self.path, 'w') as f:
            f.write(string)

    def __add__(self, obj):
        random.seed()
        inside1 = self.read()
        inside2 = obj.read()
        new_inside = inside1 + inside2
        temp_dir = tempfile.gettempdir()
        name_of_the_file = 'new_file' + str(random.randint(0, 100))
        new_path = os.path.join(temp_dir, name_of_the_file)
        new_f = File(new_path)
        new_f.write(new_inside)
        return new_f

    def __str__(self):
        return self.path

    def __getitem__(self, index):
        lst = self.read().splitlines(True)
        return lst[index]




