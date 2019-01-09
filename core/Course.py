class Course():
    def __init__(self, name, period, price, school):
        self.name = name
        self.period = period
        self.price = price
        self.school = school

    def __str__(self):
        return 'Course'

    def __repr__(self):
        return self.name


class School():
    def __init__(self,name,course):
        self.name = name
        self.course = course


if __name__ == '__main__':
    from conf.config import school_obj, course_obj
    from lib.MyPickle import MyPickle

    school_pickle_obj = MyPickle(school_obj)
    course_pickle_obj = MyPickle(course_obj)
    #
    python = Course('python', '6 month', 2000, '贵港')
    linux = Course('linux', '6 month', 1500, '贵港')
    go = Course('go', '6 month', 3000, '北京')

    guigang = Course2('贵港', [python, linux])
    print(guigang.__dict__)
    beijing = Course2('北京', [go])
    print(beijing.__dict__)
    school_pickle_obj.dump(guigang)
    school_pickle_obj.dump(beijing)
    course_pickle_obj.dump(python)
    course_pickle_obj.dump(linux)
    course_pickle_obj.dump(go)