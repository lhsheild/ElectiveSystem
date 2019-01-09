import sys
import os

sys.path.insert(0, os.path.dirname(os.getcwd()))

from core import main

if __name__ == '__main__':
    main.main()

    # from conf.config import school_obj, course_obj
    # from lib.MyPickle import MyPickle
    # from core.Course import Course,School
    #
    # school_pickle_obj = MyPickle(school_obj)
    # course_pickle_obj = MyPickle(course_obj)
    #
    # python = Course('python', '6 month', 2000, '贵港')
    # linux = Course('linux', '6 month', 1500, '贵港')
    # go = Course('go', '6 month', 3000, '北京')
    #
    # guigang = School('贵港', [python, linux])
    # print(guigang.__dict__)
    # beijing = School('北京', [go])
    # print(beijing.__dict__)
    #
    # course_pickle_obj.dump(python)
    # course_pickle_obj.dump(linux)
    # course_pickle_obj.dump(go)
    # school_pickle_obj.dump(guigang)
    # school_pickle_obj.dump(beijing)