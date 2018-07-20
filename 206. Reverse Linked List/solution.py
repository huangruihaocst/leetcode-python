# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Solution 1:
        # if head is None:
        #     return None
        # li = list()
        # node = head
        # while node:
        #     li.append(node.val)
        #     node = node.next
        # head = ListNode(li.pop())
        # node = head
        # while li:
        #     node.next = ListNode(li.pop())
        #     node = node.next
        # return head

        # Solution 2:
        # new_head = None
        # while head:
        #     next_node = head.next
        #     head.next = new_head
        #     new_head = head
        #     head = next_node
        # return new_head

        # Solution 3:
        def _reverse(h, prev=None):
            if not h:
                return prev
            curr, h.next = h.next, prev
            return _reverse(curr, h)
        return _reverse(head)


if __name__ == '__main__':
    s = Solution()
    n = ListNode(1)
    n.next = ListNode(2)
    n.next.next = ListNode(3)
    n.next.next.next = ListNode(4)
    n.next.next.next.next = ListNode(5)
    print(s.reverseList(n).val)
