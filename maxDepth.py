class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = Solution.maxDepth(self,root.left)
        right = Solution.maxDepth(self,root.right)
        if left == 0 and right != 0:
            print(type(left))
            left = left + 1
        if right == 0 and left != 0:
            right = right + 1
        print(max(left, right) + 1)
        print(type(left))
        return max(left, right) + 1

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

     def __str__(self):
        return str(self.val)

#[3,9,20,null,null,15,7]

input_3=TreeNode(3)
input_4=TreeNode(4)
input_5 = TreeNode(5)
input_5.left=input_3
input_5.right=input_4
input_18 = TreeNode(18)
input_all = TreeNode(2)
input_all.left = input_5
input_all.right = input_18
slu_ = Solution()
print(input_all)
t = slu_.maxDepth(input_all)
print(t)

#Solution.maxDepth(root=TreeNode)
