# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def initList(self, data):
        # 判断是否为空
        if len(data) == 0:
            return
        else:
            # 创建头结点
            self.head = ListNode(data[0])
            r = self.head
            p = self.head
            # 逐个为 data 内的数据创建结点, 建立链表
            for i in data[1:]:
                node = ListNode(i)
                p.next = node
                p = p.next
            return r

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not (l1 and l2):
            return l1 if l1 else l2

        if l1.val <= l2.val:
            l1.next = Solution().mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = Solution().mergeTwoLists(l1,l2.next)
            return l2

    def mergeTwoLists_j(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not (l1 and l2):
            return l1 if l1 else l2
        p = h = ListNode(None)
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next

        p.next = l1 if l1 else l2

        return h.next

    def listnode_result(self, ListNode):
        while ListNode:
            print(ListNode.val, end='')
            ListNode = ListNode.next
            if ListNode:
                print('->', end='')


if __name__ == "__main__":
    test = Solution()
    data1 = [2]
    data2 = [1]
    l1 = test.initList(data1)
    l2 = test.initList(data2)
    result = test.mergeTwoLists_j(l1, l2)
    result = test.listnode_result(result)
