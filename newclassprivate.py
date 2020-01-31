class Person(object):
    # 构造函数
    def __init__(self, name):
        self.name = name
        self.__age = 18


obj = Person("lily")
print(obj.name)


class Student(Person):
    def __init__(self,name):
        Person.__init__(self,name)
        self.__gender = 'male'


stu = Student('lily')
print(stu._Student__gender)
print(stu.name)
print(stu._Person__age)