#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 返回能创建的房屋数
# @param t int整型 要建的房屋面宽
# @param xa int整型一维数组 已有房屋的值，其中 x0 a0 x1 a1 x2 a2 ... xi ai 就是所有房屋的坐标和房屋面宽。 其中坐标是有序的（由小到大）
# @return int整型
#
class Solution:
    def __init__(self):
        self.ans = 0
        self.location = []

    def getHouses(self, t, xa):
        for i in range(0, len(xa), 2):
            self.location.append((xa[i], xa[i + 1]))
        self.location.sort(key=lambda x: x[0])
        for i in range(1, len(self.location)):
            x, a = self.location[i]
            x_, a_ = self.location[i - 1]
            if 2 * x - a - 2 * x_ - a_ == 2 * t:
                self.ans += 1
            elif 2 * x - a - 2 * x_ - a_ > 2 * t:
                self.ans += 2
        return self.ans + 2