import pickle
import os


class MyPickle():
    def __init__(self, file_path):
        self.file_path = file_path

    def dump(self, obj):
        with open(self.file_path, 'ab') as f:
            pickle.dump(obj, f)

    def load_iter(self):
        with open(self.file_path, 'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    yield obj
                except:
                    break

    def edit(self, obj):  # 编辑pickle文件中的对象
        f2 = MyPickle(self.file_path+'.bak')
        for item in self.load_iter():
            if item.name == obj.name:
                f2.dump(obj)
            else:
                f2.dump(item)
        os.remove(self.file_path)
        os.rename(self.file_path+'.bak', self.file_path)

    def load_obj(self):
        obj_list = []
        with open(self.file_path, 'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    obj_list.append()

                except:
                    return obj_list
        return obj_list


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
