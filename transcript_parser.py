import re
import os
import glob

path = r"E:\Users\Trenton J. McKinney\PycharmProjects\UDACITY\01_Data_Analyst\05_R_Data_Analysis\Subtitles\L3_ Explore One Variable (4 hrs) Subtitles"

files = glob.glob(f'{path}/*.srt')

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
