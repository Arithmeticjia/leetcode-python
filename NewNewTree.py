'''
树的构建：
     3
  9     20
     15    7
'''
class Tree():
    '树的实现'
    def __init__(self,data = None,left = None,right = None):
        self.left = left
        self.right = right
        self.data = data

    def __str__(self):
        return str(self.data)


# test tree


# 方法二
list=[9,3,15,20,7]
tree=Tree(list)

def level_print(tree):
    if tree==None:
        return
    q=[]
    q.append(tree)
    results={}
    level=0
    current_level_num=1
    nextlevelnum=0
    d=[]
    while q:
        current=q.pop(0)
        current_level_num-=1
        d.append(current.data)
        if current.left!=None:
            q.append(current.left)
            nextlevelnum+=1
        if current.right!=None:
            q.append(current.right)
            nextlevelnum+=1
        if current_level_num==0:
            current_level_num=nextlevelnum
            nextlevelnum=0
            results[level]=d
            d=[]
            level+=1
    print(results)



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

def PrintFromTopToBottom(root):
    # 设置答案集合ans 临时数组temp,使用temp存储需要打印的节点
    if not root:
        return []
    ans = []
    temp = []
    temp.append(root)
    while temp:
        currentRoot = temp.pop(0) #获当前取需要打印的节点
        ans.append(currentRoot.data)
        if currentRoot.left: #将左右子节点存入temp等待打印 t
            temp.append(currentRoot.left)
        if currentRoot.right:
            temp.append(currentRoot.right)
    print(ans)
    return ans

def traverse(root):  # 层次遍历
    if root is None:
        return None
    q = [root]
    res = [root.data]
    while q != []:
        pop_node = q.pop(0)
        if pop_node.left is not None:
            q.append(pop_node.left)
            res.append(pop_node.left.data)

        if pop_node.right is not None:
            q.append(pop_node.right)
            res.append(pop_node.right.data)
    print(res)
    return res
function(tree)
traverse(Tree)
#level_print(Tree)
PrintFromTopToBottom(Tree)

