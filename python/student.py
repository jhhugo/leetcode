# -*- coding:utf-8 -*-
if __name__ == '__main__':
    class Scl_Person(object):
        def __init__(self, name, age, ide=None, ocp=None):
            self.name = name
            self.age = age
            self.ide = ide
            self.ocp = ocp
        
        def __setattr__(self, name, value):
            if (name == 'age' or 'name') and (name in self.__dict__.keys()):
                raise TypeError('属性为只读')
            else:
                self.__dict__[name] = value

        def eat(self):
            print("%s在吃饭" % self)
        
        def sleep(self):
            print("%s在睡觉" % self)

    class Scl_Student(Scl_Person):
        def __init__(self, name, age, ide):
            super().__init__(name, age, ide)

        def __str__(self):
            return '学号为%s,年龄为%s的%s同学' % (self.ide, self.age, self.name)

        def study(self):
            print('%s在学习' % self)
        
    class Scl_Captain(Scl_Student):
        def __init__(self, name, age, ide, ocp):
            super(Scl_Student, self).__init__(name, age, ide, ocp)

        def charge(self):
            print('%s在管理同学' % self)

        def __str__(self):
            return '学号为%s,年龄为%s的%s%s' % (self.ide, self.age, self.name, self.ocp)

    class Scl_teacher(Scl_Person):
        def __str__(self):
            return '年龄为%s的%s%s' % (self.age, self.name, self.ocp)
        def __init__(self, name, age, ocp):
            super().__init__(name, age, ocp)

        def teach(self):
            print('%s在教学' % self)

        def tec_charge(self):
            print('%s在管理学生' % self)
        
    stu = Scl_Student('hugo', 18, 1314)
    cap = Scl_Captain('lyj', 18, 1315, '组长')
    tec = Scl_teacher('pao', 18, '教师')
    stu.eat()
    stu.sleep()
    stu.study()
    cap.eat()
    cap.sleep()
    cap.study()
    cap.charge()
    tec.eat()
    tec.sleep()
    tec.teach()
    tec.tec_charge()
    # stu.name = 'xiaolaba'