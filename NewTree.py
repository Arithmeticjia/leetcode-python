'''
树的构建：
     3
  9     20
     15    7
'''


class Tree():
    '树的实现'
    def __init__(self,left = 0,right = 0,data = 0):
        self.left = left
        self.right = right
        self.data = data

    def __str__(self):
        return str(self.data)
# test tree


tree1 = Tree(data=15)
tree2 = Tree(data=7)
tree3 = Tree(tree1,tree2,data=20)
tree4 = Tree(data=9)
base = Tree(tree4,tree3,3)
Tree = Tree(base)


def function(root):
    A = []
    result = []
    if not root:
        return result
    A.append(root)
    while A:
        current_root = A.pop(0)
        result.append(current_root.data)
        if current_root.left:
            A.append(current_root.left)
        if current_root.right:
            A.append(current_root.right)
    print(result)
    return result


function(Tree)

