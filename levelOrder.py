class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
    3
   / \
  9  20
    /  \
   15   7
'''


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        currentStack = [root]
        outList= []
        while currentStack:
            nextStack = []
            tmp = []
            for point in currentStack:
                if point.left:
                    nextStack.append(point.left)
                if point.right:
                    nextStack.append(point.right)
                tmp.append(point.val)
            outList.append(tmp)
            currentStack = nextStack
            # print(type(currentStack),currentStack)

        return outList


n1 = TreeNode(3)
n2 = TreeNode(9)
n3 = TreeNode(20)
n4 = TreeNode(15)
n5 = TreeNode(7)
n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5
s = Solution()
result = s.levelOrder(n1)
print(result)