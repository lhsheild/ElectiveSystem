import os


local_path = os.path.dirname(os.getcwd())

userinfo = os.path.abspath(os.path.join(local_path, 'db/userinfo'))
schoolinfo = os.path.abspath(os.path.join(local_path, 'db/schoolinfo'))
teacher_obj = os.path.abspath(os.path.join(local_path, 'db/teacher_obj'))
classes_obj = os.path.abspath(os.path.join(local_path, 'db/classes_obj'))
course_obj = os.path.abspath(os.path.join(local_path, 'db/course_obj'))