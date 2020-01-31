class people:

    name = ''     # 定义基本属性
    age = 0
    sex = ''
    __weight = 0  # 定义私有属性,私有属性在类外部无法直接进行访问

    # 定义构造方法
    def __init__(self, n, a, w ,s):
        self.name = n
        self.age = a
        self.sex = s
        self.__weight = w
        self.__height = 180

    def information(self):
        print("%s is a %d yesrs old %s and weights %skg" % (self.name, self.age, self.sex, self.__weight))



class Programmer(people):
    language = ''

    def __init__(self,n, a, w, s, l):
        # 调用父类的构函
        people.__init__(self, n, a, w, s)
        self.language = l
        # 重写父类的方法

    def information(self):
        print("%s is a %d yesrs old %s and weights %dkg.He uses %s" % (self.name, self.age, self.sex, self._people__weight,self.language))


if __name__ == '__main__':
    # 实例化类
    p = people('Mike', 25, 60, 'man')
    print(p._people__weight)
    q = Programmer('Mike', 25, 60, 'man', 'python')
    p.information()
    q.information()