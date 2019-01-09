from conf.config import *
from lib import MyPickle
from core.Teacher import Teacher


class Manager():
    menu = [('创建讲师帐号', 'create_teacher'), ('查看讲师', 'show_teacher'), ('创建学生帐号', 'create_student'), ('创建课程', ' create_course'),
            ('查看课程', 'show_course'), ('创建班级', 'create_classes'), ('查看班级', 'show_classes'), ('绑定班级', 'bound_classes'),
            ('创建学校', ' create_school'), ('查看学校', 'show_school'), ('退出', 'exit')]

    @staticmethod
    def userinfo_handler(content):  # 用户信息写入文件的方法抽象出来并作为类的静态方法
        with open(userinfo, 'a') as f:
            f.write('\n{}'.format(content))

    def __init__(self, name):
        self.name = name

        self.teacher_pickle_obj = MyPickle.MyPickle(teacher_obj)
        self.course_pickle_obj = MyPickle.MyPickle(course_obj)
        self.school_pickle_obj = MyPickle.MyPickle(schoolinfo)
        self.class_pickle_obj = MyPickle.MyPickle(classes_obj)

    def show(self, pickle_obj):
        pickle_obj = getattr(self, pickle_obj)
        load_iter = pickle_obj.load_iter()
        for obj in load_iter:
            for i in obj.__dict__:
                print(i, obj.__dict__[i])
        print('=' * 50)

    def create_teacher(self):
        print('开始创建教师用户')
        teacher_name = input('输入教师用户名:')
        teacher_pwd = input('输入教师用户密码:')
        self.show_school()
        school = input('输入教师对应校区:')
        content = '{}|{}|Teacher'.format(teacher_name, teacher_pwd)
        Manager.userinfo_handler(content)
        teacher = Teacher(teacher_name, school)
        self.teacher_pickle_obj.dump(teacher)
        print('教师"{}"创建成功'.format(teacher.name))

    def create_student(self):
        pass

    def show_teacher(self):
        self.show('teacher_pickle_obj')

    def show_course(self):
        self.show('course_pickle_obj')

    def show_school(self):
        self.show('school_pickle_obj')

    def show_classes(self):
        self.show('class_pickle_obj')
