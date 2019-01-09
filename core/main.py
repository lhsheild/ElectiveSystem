import sys

from conf.config import *
from core.Manager import Manager
from core.Teacher import Teacher


def login():
    usr = input('username:')
    pwd = input('password:')
    with open(userinfo) as f:
        for line in f:
            username, password, role = line.strip().split('|')
            if username == usr and password == pwd:
                print('\033[1;32m登录成功!\033[0m')
                return {'username': username, 'role': role}
        else:
            print('\033[1;32m登录失败!\033[0m')


def main():
    '''打印欢迎信息'''
    print('\033[0;36m欢迎使用本系统\033[0m')
    '''login,得到返回值:用户姓名,身份'''
    login_ret = login()  # {'username': lh, 'role:': Manager}
    '''用户对应视图,用户调用任何方法应通过角色对象调用'''
    if login_ret:
        role_class = getattr(sys.modules[__name__], login_ret['role'])  # 已经将不同角色类(Manager...)导入本模块,
        # 因此可以根据login_ret中角色字符串反射到对应类
        obj = role_class(login_ret['username'])  # 实例化对应类
        while True:
            for i, j in enumerate(role_class.menu, 1):
                print(i, j[0])
            # try:
            func_ret = int(input('输出操作符:'))
            if hasattr(obj, role_class.menu[func_ret - 1][1]):
                getattr(obj, role_class.menu[func_ret - 1][1])()
            else:
                print('没有该功能!')
            # except:
            #     print('操作有误!')


if __name__ == '__main__':
    print(sys.modules[__name__])