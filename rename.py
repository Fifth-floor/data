import os
import json

def get_file_name(path):
    result = os.path.splitext(path)[0]
    result = result[result.rfind('/') + 1:]
    return result


def is_valid_image(name):
    name = name.lower()

    return name.endswith('jpeg') or name.endswith('jpg') or name.endswith('png')


def get_files(path):
    f_total = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        f_total.extend(filenames)
        break

    f_total = [f'{path}{x}' for x in f_total if is_valid_image(x)]
    # print(f_total)
    return f_total


folder = 'old_hi'
path = f'D:/Git/5f/data/{folder}/'

f_total = get_files(path)
for f in f_total:
    if not is_valid_image(f):
        print('remove', f)
        os.remove(f)

f_total = get_files(path)
for i, f in enumerate(f_total):
    # print('rename', f'{path}qqtemp_{i}.jpg')
    os.rename(f, f'{path}qqtemp_{i}.jpg')

max_index = 0
f_total = get_files(path)
for i, f in enumerate(f_total):
    # print('rename', f'{path}qqtemp_{i}.jpg')
    os.rename(f, f'{path}{i}.jpg')
    max_index = i

with open('index.json', encoding='utf-8') as f:
    index_record = json.load(f)

index_record[folder] = max_index
print(index_record)

with open('index.json', 'w', encoding='utf-8',) as f:
    json.dump(index_record, f, indent=4, ensure_ascii=False)
