# -*- coding:utf-8 -*-
if __name__ == '__main__':
    # a = (x**2 for x in range(0, 10))
    # print(a,type(a))

    # a = set((1, 2, 3, 4, 5))
    # print(a, type(a))
    # result = a.add(6)
    # b = set([6, 7, 8])
    # a.add(b)
    # print('new a: ', a, result)

    # result = a.pop()
    # print(result, a)

    # s1 = {1, 2, 3, 4}
    # s2 = frozenset([7, 8, 9])
    # # result = s1.intersection_update(s2)
    # s1.update({1, 2, 5})
    # print(s1)
    
    # s1 = {1, 2, 3, 4}
    # s2 = set([15, 2])
    # # result = s1 - s2
    # # s1.difference_update(s2)
    # # print(s1)
    # # s1.intersection_update(s2)
    # # print(s1)
    # s1.update(s2)
    # print(s1)
    import time
    # a = time.time()
    # print(time.localtime(a - 489498.654654)) #获取本地计算机时间
    # t = time.time()
    # print(time.ctime(t))
    # time_tuple = time.localtime()
    # print(time.asctime(time_tuple))
    # time_str = time.strftime('%Y - %m - %d  %H:%M:%S', time.localtime())
    # print(time_str)
    # pt = time.strptime('2018 - 08 - 27  17:24:38', '%Y - %m - %d  %H:%M:%S')
    # print(pt)
    # print(time.strftime('%H:%M:%S', time.localtime()))
    # time.sleep(3)
    # print('完成休眠')
    # import calendar
    # print(calendar.month(2017, 6))
    import datetime
    # print(datetime.datetime.now())
    # print(datetime.datetime.today())
    # td = datetime.datetime.now()
    # re = td + datetime.timedelta(days=7)
    # print(td)
    # print(re)
    # first = datetime.datetime(2017,9,18)
    # second = datetime.datetime(2017, 9, 20)
    # print(second - first)
    # print((second - first).total_seconds())
    # td = datetime.datetime.now()
    # print(td)
    # td_timestamp = datetime.datetime.timestamp(td)
    # print(td_timestamp)
    # td_utc = time.time()
    # print(td_utc)
    # td = datetime.datetime.fromtimestamp(1535364679.242193)
    # print(td)
    # uct = datetime.datetime.utcfromtimestamp(1535364679.242193)
    # print(uct)
    # now = datetime.datetime.now()
    # dt = now.strftime('%Y/%m/%d %H:%M:%S')
    # print(dt)
    # td = datetime.datetime.now()
    # time.sleep(10)
    # td_1 = datetime.datetime.now()
    # tz = datetime.timezone(datetime.timedelta(hours=8))
    # td = td.replace(tzinfo=tz)
    # print(td)
    # from datetime import datetime,timedelta,timezone
    # td = datetime.utcnow()
    # print(td)
    # td = td.replace(tzinfo=timezone(timedelta(hours=0)))
    # print(td)
    # bj_td = td.astimezone(timezone(timedelta(hours=8)))
    # print(bj_td)
    # usa_td = td.astimezone(timezone(timedelta(hours=12)))
    # print(usa_td)
    # bj_td_1 = usa_td.astimezone(timezone(timedelta(hours=8)))
    # print(bj_td_1)
    # def add(a, b, c):
    #     print((a + b) * c)
    # add(1, 2, 3)
    # import functools
    # # add2 = functools.partial(add, c=2)
    # # add2(1, 2)
    # int2 = functools.partial(int, base=2)
    # a = int2('11000')
    # print(a)
    # 闭包
    # def sum(a, b):
    #     def func():
    #         print(a + b)
    #     return func
    # new = sum(10, 10)
    # new()
    # def test():
    #     funcs = []
    #     def test2(num):
    #         def inner():
    #             print(num)
    #         return inner
    #     for i in range(1, 4):
    #         funcs.append(test2(i))
    #     return funcs
    # newfuncs = test()
    # newfuncs[0]()
    # newfuncs[1]()
    # newfuncs[2]()
    # def check(func):
    #     def inner():
    #         print('登录验证....')
    #         func()
    #     return inner
    
    # def check1(func):
    #     def inner():
    #         print('-' * 30)
    #         func()
    #     return inner

    # @check
    # @check1
    # def fss():
    #     print('发说说')
    # fss()
    # def zsq(func):
    #     def inner(*args, **kwargs):
    #         print('*' * 30)
    #         res = func(*args,**kwargs)
    #         return res
    #     return inner
    # @zsq
    # def pnum(num, num2, a):
    #     print(num, num2, a)
    # pnum(1, 2, a = 13)
    # with open(r'.\python\a.txt', 'w') as f:
    #     f.write("12345")
    # with open(r'.\python\a.txt', 'r+') as f:
    #     cont = f.read()
    #     print(cont)
    #     new_cont = f.write("123abc")
    # with open(r'.\python\a.txt', 'r') as f:
    #     print(f.tell())
    #     f.seek(2)
    #     print(f.tell())
    #     print(f.read(-1))
    #     print(f.tell())
    # f.readable()#判断可读性
    # with open(r'.\python\a.txt', 'r') as f:
    #     cont = 1
    #     while(cont):
    #         cont = f.readline()
    #         print(cont, end='')
    # import shutil,os
    # # shutil.copyfile(r'.\python\a.txt',  r'.\python\b.txt')
    # # os.remove(r'.\python\b.txt')
    # # print(os.getcwd())
    # # # os.chdir(r'.\python')
    # # # print(os.getcwd())
    # # print(os.listdir('.'))
    # # print(os.path.abspath('.'))
    # # path = os.path.abspath('.')
    # # os.mkdir(path + r'\python\test')
    # # path = os.path.join(os.path.abspath('.'), r'python\a.txt')
    # # print(os.path.split(path))
    # class Person(object):
    #     age = 18
    # p = Person()
    # p.list = ['aad', '2323']
    # p.age = 20
    # # del p.list#删去
    # # print(p.__dict__)#打印所有属性字典
    # print(p.age)
    # print(p.__class__)#使对象指向哪个类
    # class Peee(object):
    #     def eat(self,)
    # class Person(object):
    #     def eat2(self):
    #         print('这个是实例方法', self)

    #     @classmethod
    #     def leifangfa(cls):
    #         print('这个是类方法', cls)
    #     @staticmethod
    #     def jingtaifangfa():
    #         print('这是静态方法')
    # p = Person()
    # print(p)
    # p.eat2()
    # p.jingtaifangfa()
    # class Person(object):
    #     def funcname(self, parameter_list):
    #         raise NotImplementedError
    # class Person(object):
    #     age = 0
    #     def shilifangfa(self):
    #         print(self)
    #         print(self.age)
    #         print(self.num)#实例对象可以访问自己的属性也可以访问类的属性，
    #                        #类不能访问到实例的属性和方法
    #     @classmethod
    #     def leifangfa(cls):
    #         print(cls)
    #         print(cls.age)
    #         print(cls.num)#静态方法可以访问所有
    
    # p = Person()
    # p.num = 10
    # print(p.shilifangfa())
    # print(p.leifangfa())
    # class Person(object):
    #     def __init__(self, age):
    #         self.__age = age

    #     # def set_age(self, value):
    #     #     self.__age = value
    #     # age = property(fset=set_age)
    #     @property
    #     def age(self):
    #         raise AttributeError('只写属性')
    #     @age.setter
    #     def set_age(self, value):
    #         self.__age = value
    #     def __get

    # p = Person(18)
    # print(p.age)
    # class hugo(object):
    #     """[summary]
        
    #     Arguments:
    #         object {[type]} -- [description]
    #     """
       
    #     def __init__(self, value):
    #         print('初始化')
    #         self.age h     ggggg= value
    #     def __del__(self):
    #         print('被释放了')
    
    # p = hugo(18)
    # print(p)
    # print(p.age)
    # class Person(object):
    #     __personcount = 0
    #     def __init__(self):
    #         print('增加一个人')
    #         Person.__personcount += 1
    #     def __del__(self):
    #         print('减少一个人')
    #         self.__class__.__personcount -= 1
    #     @classmethod
    #     def log(cls):
    #         print('当前还有多少个人： %s' % cls.__personcount)
    
    # p1 = p2 = Person()
    # # p2 = Person()
    # # Person.log()
    # # del p1
    # # Person.log()
    # import sys
    # print(sys.getrefcount(p1)) #内存引用计数器
    # del p2
    # print(sys.getrefcount(p1))
    # import objgraph
    # import gc
    # class Person(object):
    #     pass
    # class Dog(object):
    #     pass
    
    # p = Person()
    # d = Dog()
    # p.pet = d
    # d.master = p
    # print(objgraph.count('Person'))
    # print(objgraph.count('Dog'))

    # del p
    # del d
    # gc.collect() #立刻触发垃圾回收
    # print(objgraph.count('Person'))
    # print(objgraph.count('Dog'))
    # import functools
    import win32com.client
    # speaker = win32com.client.Dispatch('SAPI.SpVoice')
    # speaker.Speak('我是喇叭咯哆')
    # class Calculator(object):
    #     def __check_num(func):
    #         # @functools.wraps(func)
    #         def inner(self, n):
    #             if not isinstance(n, int) and not isinstance(n, float):
    #                 raise TypeError('请输入一个数')
    #             return func(self, n)
    #         return inner
        
    #     def __say(self, word):
    #         speaker = win32com.client.Dispatch('SAPI.SpVoice')
    #         speaker.Speak(word)

    #     def __creat_say(s=''):
    #         def say(func):
    #             def inner(self, num):
    #                 self.__say(s + str(num))
    #                 return func(self, num)
    #             return inner
    #         return say


    #     @__check_num
    #     @__creat_say('初始化')
    #     def __init__(self, num):
    #         self.__result = num 

    #     @__check_num
    #     @__creat_say('加上')
    #     def jia(self, num):
    #         self.__result += num
    #         return self

    #     @__check_num
    #     @__creat_say('减去')
    #     def jian(self, num):
    #         self.__result -= num
    #         return self

    #     @__check_num
    #     @__creat_say('乘以')
    #     def cheng(self, num):
    #         self.__result *= num
    #         return self

    #     @__check_num
    #     @__creat_say('除以')
    #     def chu(self, num):
    #         self.__result /= num
    #         return self

    #     def show(self):
    #         self.__say("计算结果" + str(self.__result))
    #         print('计算结果为：%f' % self.__result)
    #         return self

    #     @property
    #     def reslut(self):
    #         return self.__result

    # a = Calculator(2)
    # a.jia(9).jian(1).cheng(100).chu(10).show()
    # print(a.reslut)
    # import abc
    # class Animal(object,metaclass=abc.ABCMeta):
    #     @abc.abstractmethod
    #     def jiao(self):
    #         pass

    # class Dog(Animal):
    #     def __init__(self):
    #         pass
    #     def jiao(self):
    #         print("汪汪汪")
    # class Cat(Animal):
    #     def __init__(self):
    #         pass
    #     def jiao(self):
    #         print("喵喵喵")

    # def test(obj):
    #     obj.jiao()
        
    # d = Dog()
    # c = Cat()
    # a = Animal()
    # test(d)
    # test(c)
#     import abc
#     class Animal(object, metaclass=abc.ABCMeta):
#         def __init__(self, name, age=1):
#             self.name = name
#             self.age = age

#         def eat(self):
#             print('%s在吃饭' % self)
        
#         def sleep(self):
#             print("%s在睡觉" % self)
        
#         def play(self):
#             print('%s在玩' % self)
        
#         def work(self):
#             pass

#         # def __str__(self):
#         #     return "名字是%s，年龄是%s的%s" % (self.__name, self.__age, self.__class__.__catogry)
#     class Dog(Animal):
#         def __str__(self):
#             return "名字是%s，年龄是%s的小狗" % (self.name, self.age)
        
#         def work(self):
#             print('%s看家' % self)

#     class Cat(Animal):
#         def __str__(self):
#             return "名字是%s，年龄是%s的小猫" % (self.name, self.age)
        
#         def work(self):
#             print('%s抓老鼠' % self)
        
#     class Person(Animal):
#         def __init__(self, name, pets, age=1):
#             super().__init__(name, age)
#             self.__pet = pets

#         def feed(self):
#             for p in self.__pet:
#                 p.eat()
#                 p.sleep()
#                 p.play()
            
#         def pet_work(self):
#             for p in self.__pet:
#                 p.work()

# dog = Dog('uzi')   
# cat = Cat('小猪')     
# p1 = Person(name='hugo', age=25, pets=[dog, cat])
# p1.feed()
# p1.pet_work()