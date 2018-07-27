# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Solution 1: Extra space
        # i, j = l1, l2
        # head = ListNode(float('-inf'))
        # p = head
        # while i is not None and j is not None:
        #     if i.val >= j.val:
        #         p.next = ListNode(j.val)
        #         j = j.next
        #     else:
        #         p.next = ListNode(i.val)
        #         i = i.next
        #     p = p.next
        # if i is None:
        #     p.next = j
        # if j is None:
        #     p.next = i
        # return head.next

        # Solution 2: In place
        i, j = l1, l2
        head = ListNode(float('-inf'))
        p = head
        while i is not None and j is not None:
            if i.val >= j.val:
                p.next = j
                j = j.next
            else:
                p.next = i
                i = i.next
            p = p.next
        if i is None:
            p.next = j
        if j is None:
            p.next = i
        return head.next


if __name__ == '__main__':
    s = Solution()
    n1 = ListNode(1)
    n1.next = ListNode(2)
    n1.next.next = ListNode(4)
    n2 = ListNode(1)
    n2.next = ListNode(3)
    n2.next.next = ListNode(4)
    n = s.mergeTwoLists(n1, n2)
    print(n.val)
    print(n.next.val)
    print(n.next.next.val)
    print(n.next.next.next.val)
    print(n.next.next.next.next.val)
    print(n.next.next.next.next.next.val)
