import pickle
import os


def dump(obj, file_path):  # 序列号pickle存入文件
    with open(file_path, 'ab') as f:
        pickle.dump(obj, f)


def load_iter(file_path):  # 读取pickle文件的生成器
    with open(file_path, 'rb') as f:
        while True:
            try:
                obj = pickle.load(f)
                yield obj
            except:
                break


def edit(obj, file_path):  # 编辑pickle文件中的对象
    for item in load_iter(file_path + '.bak'):
        if item.name == obj.name:
            dump(obj, file_path)
        else:
            dump(item, file_path)
    os.remove(file_path)
    os.rename(file_path + '.bak', file_path)
