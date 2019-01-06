import pickle


def dump(obj, file_path):
    with open(file_path, 'ab') as f:
        pickle.dump(obj, f)


def get_load_iter(file_path):
    with open(file_path, 'rb') as f:
        for obj in pickle.load(f):
            yield obj
