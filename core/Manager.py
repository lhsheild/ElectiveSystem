import sys

from conf.config import *
from lib import MyPickle
from core.Teacher import Teacher
from core.Classes import Classes
from core.Course import Course
from core.Student import Student


class Manager():
    menu = [('创建讲师帐号', 'create_teacher'), ('查看讲师', 'show_teacher'), ('创建学生帐号', 'create_student'), ('创建课程', 'create_course'),
            ('查看课程', 'show_course'), ('创建班级', 'create_classes'), ('查看班级', 'show_classes'), ('绑定班级', 'bound_class_teacher'),
            ('创建学校', ' create_school'), ('查看学校', 'show_school'), ('退出', 'exit')]

    @staticmethod
    def userinfo_handler(content):  # 用户信息写入文件的方法抽象出来并作为类的静态方法
        with open(userinfo, 'a') as f:
            f.write('\n{}'.format(content))

    def __init__(self, name):
        self.name = name

        self.teacher_pickle_obj = MyPickle.MyPickle(teacher_obj)
        self.course_pickle_obj = MyPickle.MyPickle(course_obj)
        self.school_pickle_obj = MyPickle.MyPickle(school_obj)
        self.class_pickle_obj = MyPickle.MyPickle(classes_obj)

    def show(self, pickle_obj):
        pickle_obj = getattr(self, pickle_obj)
        load_iter = pickle_obj.load_iter()
        for obj in load_iter:
            print(obj.name)
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
        print('开始创建学生用户')
        student_name = input('请输入学生姓名:')
        student_pwd = input('请输入学生密码:')
        self.show_school()
        student_school = input('请输入学生对应学校:')
        self.show_classes()
        student_class = input('请输入学生班级:')
        class_obj = self.class_pickle_obj.load_iter()
        for clas in class_obj:
            if clas.name == student_class:
                print('111')
                content = '{}|{}|Student'.format(student_name, student_pwd)
                Manager.userinfo_handler(content)
                student_obj = Student(student_name, student_school, clas)
                MyPickle.MyPickle(clas.student_path).dump(student_obj)
                print('学生"{}"创建成功'.format(student_obj.name))
                break
        else:
            print('输入有误,创建学生失败')

    def create_classes(self):
        print('开始创建班级')
        class_name = input('请输入班级名称:')
        self.show_school()
        school_name = input('请输入学校名称:')
        self.show_course()
        course = input('请输入学科名称:')
        student_path = os.path.join(student_info, class_name)
        open(student_path, 'w').close()
        clas = Classes(school_name, class_name, course, student_path)
        self.class_pickle_obj.dump(clas)
        print('班级{}创建成功'.format(clas.name))

    def show_teacher(self):
        self.show('teacher_pickle_obj')

    def show_course(self):
        self.show('course_pickle_obj')

    def show_school(self):
        self.show('school_pickle_obj')

    def show_classes(self):
        self.show('class_pickle_obj')

    def bound_class_teacher(self):
        print('绑定班级和讲师对应关系')
        self.show_classes()
        class_name = input('请输入指定班级:')
        self.show_teacher()
        teacher_name = input('请输入指定讲师:')
        teacher_g = self.teacher_pickle_obj.load_iter()
        t_o_list = []
        for obj in teacher_g:
            t_o_list.append(obj)
        for i in t_o_list:
            if i.name == teacher_name:
                i.classes.append(class_name)
                self.teacher_pickle_obj.edit(i)
                print('班级{}与讲师{}绑定成功'.format(class_name, teacher_name))
                break
        else:
            print('输入有误,绑定失败')

    def exit(self):
        sys.exit(0)
