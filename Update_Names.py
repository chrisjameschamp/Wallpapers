from os import listdir, rename
from os.path import isfile, join
from pathlib import Path

path = f'{Path(__file__).parent}/Images'

files = [f for f in listdir(path) if isfile(join(path, f))]

new_files = []
i = 0

for file in files:
    if file.startswith('CWP'):
        if int(file.split('_')[1].split('.')[0]) > i:
            i = int(file.split('_')[1].split('.')[0])
    elif not file.startswith('.'):
        new_files.append(file)

for file in new_files:
    format = file.split('.')[1]
    i += 1
    id = '{:04d}'.format(i)
    rename(f'{path}/{file}',f'{path}/CWP_{id}.{format}')