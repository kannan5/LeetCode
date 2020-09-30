# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        init_iter = 0
        first = l1
        last = l2
        NewNode, NextIter = None, None
        while first is not None and last is not None:
            if init_iter == 0:
                if first.val < last.val:
                    NewNode = ListNode(first.val, ListNode(last.val))
                else:
                    NewNode = ListNode(last.val, ListNode(first.val))
                init_iter += 1
                NextIter = NewNode
                NextIter = NextIter.next
            else:
                if first.val < last.val:
                    NextIter.next = ListNode(first.val, ListNode(last.val))
                else:
                    NextIter.next = ListNode(last.val, ListNode(first.val))
                NextIter = NextIter.next.next
            first = first.next
            last = last.next
        return NewNode

    def printList(self, list1):
        cur = list1
        while cur is not None:
            print(cur.val)
            cur = cur.next


if __name__ == '__main__':
    a = Solution()
    l1 = ListNode(1,(ListNode(2,ListNode(4))))
    l2 = ListNode(1,(ListNode(2,ListNode(3))))
    l3 = a.mergeTwoLists(l1, l2)
    a.printList(l3)
