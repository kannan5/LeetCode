class listNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def swap_pairs(self, head):
        if not head or  head.next is None:
            return head
        else:
            pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next

    def swapPairs_rec(self, head):
        if not head or not head.next: return head
        new_start = head.next.next
        head, head.next = head.next, head
        head.next.next = self.swapPairs_rec(new_start)
        return head

    
a = Solution()

l1 = listNode(1,listNode(2, listNode(3, listNode(4))))

#a.swap_pairs(l1)
a.swapPairs_rec(l1)

