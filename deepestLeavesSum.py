# Definition for a binary tree node.
'''
给你一棵二叉树，请你返回层数最深的叶子节点的和
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.deepest = -1
        self.sum = 0

    def deepestLeavesSum(self, root: TreeNode) -> int:

        def dfs(node, level):
            if node is None:
                return
            if node.left is None and node.right is None:
                if self.deepest < level:
                    self.sum = node.val
                    self.deepest = level
                elif self.deepest == level:
                    self.sum += node.val

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return self.sum
