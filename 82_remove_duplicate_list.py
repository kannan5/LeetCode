class ListNode:
    def __init__(self, value = 0, next = None):
        self.val = value
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        if head.next is None:
            return head 
        
        prev = head
        curr = head.next
        while curr:
            if curr.val == prev.val:
                prev.next = curr.next
                curr = curr.next
            curr = curr.next
            prev = prev.next
        return head

        
        






if __name__ == "__main__":
    a = ListNode(1)
    a.next = ListNode(1)
    a.next.next = ListNode(2,ListNode(2,ListNode(3)))
    b = Solution()
    b.deleteDuplicates(a)