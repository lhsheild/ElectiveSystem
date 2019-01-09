import os


local_path = os.path.dirname(os.getcwd())

userinfo = os.path.abspath(os.path.join(local_path, 'db/userinfo'))
school_obj = os.path.abspath(os.path.join(local_path, 'db/school_obj'))
teacher_obj = os.path.abspath(os.path.join(local_path, 'db/teacher_obj'))
classes_obj = os.path.abspath(os.path.join(local_path, 'db/classes_obj'))
course_obj = os.path.abspath(os.path.join(local_path, 'db/course_obj'))

student_info = os.path.abspath(os.path.join(local_path, 'db/student_info'))


if __name__ == '__main__':
    import pickle

    with open(r'E:\Projects\Python_Projects\ElectiveSystem\db\school_obj', 'rb') as f:
        while True:
            try:
                da = pickle.load(f)
                print(da)
                print(da.__dict__)
                print(type(da))
            except:
                break
