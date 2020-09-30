class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def FindNthNode(self, head, n):
        if head.next is None:
            return
        slow, s_count = head, 1
        fast, f_count = head.next, 2
        while fast.next is not None:
            slow = slow.next
            s_count += 1
            if fast.next.next is not None:
                fast = fast.next.next
                f_count += 2
            else:
                fast = fast.next
                f_count += 1
        target = f_count - (n - 1)
        if f_count == n:
            return head.next
        while target > s_count:
            if s_count + 1 == target:
                slow.next = slow.next.next
            slow = slow.next
            s_count += 1
        return head



if __name__ == '__main__':
    # llist = ListNode(1, ListNode(2, ListNode(3, ListNode(4,ListNode(5,ListNode(6,ListNode(7)))))))
    llist = ListNode(1, ListNode(2))
    a = Solution()
    print(a.FindNthNode(llist, 2))
