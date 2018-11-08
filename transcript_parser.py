import re
import os
import glob
from natsort import natsorted

path = r"D:\PythonProjects\UDACITY\L7\en"

files = glob.glob(f'{path}/*.srt')

files = natsorted(files)

# file_name = r"16 - Limiting the Axes.srt"

for file_name in files:

    path_file_name = os.path.join(path, file_name)

    printed_name = file_name.split('\\')[-1:]

    print(printed_name[0][:-4])

    with open(path_file_name, 'r') as f:

        test = []

        for line in f:
            line = line.strip('\n')
            y = re.findall('(?i)^[a-z]', line)
            if len(y) > 0:
                test.append(line)

        print(' '.join(test))

    print('\n')
