#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 返回能创建的房屋数
# @param t int整型 要建的房屋面宽
# @param xa int整型一维数组 已有房屋的值，其中 x0 a0 x1 a1 x2 a2 ... xi ai 就是所有房屋的坐标和房屋面宽。 其中坐标是有序的（由小到大）
# @return int整型
# 2,[-1, 4, 5, 2]
#
class Solution:

    def getHouses(self, t, xa):
        location = []
        ans = 0
        # 遍历，查找房屋坐标（房屋中心坐标）
        for i in range(0, len(xa), 2):
            # 存储房子坐标和宽度
            location.append((xa[i], xa[i + 1]))
        # [[-1, 4], [5, 2]]
        # 排序
        location.sort(key=lambda x: x[0])
        print(location)
        for i in range(1, len(location)):
            # 当前房子
            x, a = location[i]
            # 前一个房子
            x_, a_ = location[i - 1]
            if 2 * x - a - 2 * x_ - a_ == 2 * t:
                ans += 1
            elif 2 * x - a - 2 * x_ - a_ > 2 * t:
                ans += 2
        return ans + 2


Solution().getHouses(2, [-1, 4, 5, 2])
