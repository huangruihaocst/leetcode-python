# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        visited = set()
        node = head
        last = None
        while node:
            if node.val not in visited:
                visited.add(node.val)
                last = node
                node = node.next
            else:
                last.next = node.next
                node = node.next
        return head


if __name__ == '__main__':
    s = Solution()
    n = ListNode(1)
    n.next = ListNode(1)
    n.next.next = ListNode(2)
    n.next.next.next = ListNode(3)
    n.next.next.next.next = ListNode(3)
    s.deleteDuplicates(n)
    print(n.val)
    print(n.next.val)
    print(n.next.next.val)
    print(n.next.next.next.val)
