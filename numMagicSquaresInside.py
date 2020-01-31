class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        grids = self.generate_matrix(grid)

        count = 0
        print(grids)
        for i in grids:
            print(self.checksame(i),self.checkmagic(i))
            if self.checkmagic(i) == True and self.checksame(i) == True:
                count = count + 1
        print(count)
        return count



    def generate_matrix(self, grid):
        all = []

        # 生成所有矩阵组合

        for n in range(len(grid[0])-2):
            temmatrix = []
            for m in range(len(grid)-2):
                tem = []
                tem.append(grid[m][n:n + 3])
                tem.append(grid[m + 1][n:n + 3])
                tem.append(grid[m + 2][n:n + 3])
                temmatrix.append(tem)
            for o in range(len(temmatrix)):
                all.append(temmatrix[o])

        return all

    def checksame(self,matrix):
        l = len(matrix)
        flag = True
        tem = []
        for g in range(l):
            for h in range(l):
                tem.append(matrix[g][h])
        print(len(set(tem)))
        for i in tem:
            if i >= 10:
                flag = False
        if len(set(tem)) == 1:
            flag = False
        print('checksame:',flag)
        return flag

    def checkmagic(self, matrix):
        l = len(matrix)

        flag = True

        # 斜
        tmp = 0
        for i in range(l):
            tmp += matrix[i][i]
        if tmp != 15:
            flag = False

        # 行
        for i in range(l):
            tmp = 0
            for j in range(l):
                tmp += matrix[i][j]
            if tmp != 15:
                flag = False
        # 列
        for i in range(l):
            tmp = 0
            for j in range(l):
                tmp += matrix[j][i]
            if tmp != 15:
                flag = False
        print('checkmagic',flag)
        return flag


if __name__ == '__main__':
    Solution().numMagicSquaresInside(
        [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
    )