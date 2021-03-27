import os
from SingleLog.log import Logger


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


logger = Logger('rename_bot', Logger.INFO)
path = f'D:/git/5floor/data/girl'


# f_total = get_files(path)
# removed = False
# for f in f_total:
#     if not is_valid_image(f):
#         logger.show('Remote', f)
#         removed = True
#         # os.remove(f)
#
# if not removed:
#     logger.show('沒有檔案被移除')

def find_max_file_name():
    f_total = get_files(path)
    max_name = 0
    for f in f_total:
        name = f[f.rfind('/') + 1:]
        name = name[4:-4]
        # logger.show(name)

        if max_name < int(name):
            max_name = int(name)
    return max_name

move_file = False

max_name = find_max_file_name()
logger.show('max name', max_name)

for i in range(max_name):

    tmp_file_name = f'D:/git/5floor/data/girl/{i}.jpg'
    if not os.path.exists(tmp_file_name):
        logger.show('檔案不存在', tmp_file_name)

        if move_file:
            current_max_name = find_max_file_name()
            if current_max_name < i:
                break
            os.rename(f'D:/git/5floor/data/girl/{current_max_name}.jpg', tmp_file_name)
