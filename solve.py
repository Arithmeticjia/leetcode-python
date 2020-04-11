class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])

        def dfs(board, i, j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] == "X" or board[i][j] == "#":
                return
            else:
                board[i][j] = "#"
            dfs(board, i - 1, j)
            dfs(board, i + 1, j)
            dfs(board, i, j + 1)
            dfs(board, i, j - 1)

        for i in range(row):
            for j in range(col):
                isEdge = False
                if i == row - 1 or j == col - 1 or i == 0 or j == 0:
                    isEdge = True
                if isEdge and board[i][j] == "O":
                    dfs(board, i, j)

        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"

        print(board)


board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
Solution().solve(board)
