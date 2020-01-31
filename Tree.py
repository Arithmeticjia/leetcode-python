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


class MyTree():
    '二叉树的实现'
    def __init__(self,base = 0):
        self.base = base

    def _Empty(self):
        '是否为空树'
        if self.base == 0:
            return True
        else:
            return False

    def qout(self,tree_base):
        '前序遍历:根-左-右'
        if tree_base == 0:
            return
        print(tree_base.data,end='')
        self.qout(tree_base.left)
        self.qout(tree_base.right)

    def mout(self,tree_base):
        '中序遍历:左-根-右'
        if tree_base == 0:
            return
        self.mout(tree_base.left)
        print(tree_base.data,end='')
        self.mout(tree_base.right)

    def hout(self,tree_base):
        '后序遍历:左-右-根'
        if tree_base == 0:
            return
        self.hout(tree_base.left)
        self.hout(tree_base.right)
        print(tree_base.data,end='')

# test tree

tree1 = Tree(data=15)
tree2 = Tree(data=7)
tree3 = Tree(tree1,tree2,data=20)
tree4 = Tree(data=9)
base = Tree(tree4,tree3,3)
MyTree = MyTree(base)
print('''
前序遍历结果:''')
MyTree.qout(MyTree.base)
print('''
中序遍历结果:''')
MyTree.mout(MyTree.base)
print('''
后序遍历结果:''')
MyTree.hout(MyTree.base)

tem = 'hello world'
print(tem[-5:0])

