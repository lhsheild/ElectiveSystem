from conf.config import *


class Manager():
    menu = [('创建讲师帐号', 'create_teacher'), ('创建学生帐号', 'create_student'), ('创建课程', ' create_course'),
            ('查看课程', 'show_course'), ('创建班级', 'create_classes'), ('查看班级', 'show_classes'), ('绑定班级', 'bound_classes'),
            ('退出', 'exit')]

    @staticmethod
    def userinfo_handler(content):  # 用户信息写入文件的方法抽象出来并作为类的静态方法
        with open(userinfo, 'a') as f:
            f.write('\n{}'.format(content))

    def __init__(self, name):
        self.name = name

    def create_teacher(self):
        print('开始创建教师用户')
        teacher_name = input('输入教师用户名:')
        teacher_pwd = input('输入教师用户密码:')
        school = input('输入教师对应校区:')
        content = '{}|{}|Teacher'.format(teacher_name, teacher_pwd)
        Manager.userinfo_handler(content)

    def create_student(self):
        pass
