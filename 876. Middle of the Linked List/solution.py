# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Solution 1:
        # cnt = 0
        # p = head
        # while p:
        #     cnt += 1
        #     p = p.next
        # half = cnt // 2
        # cnt = 0
        # p = head
        # while p:
        #     if cnt == half:
        #         return p
        #     cnt += 1
        #     p = p.next

        # Solution 2:
        # nodes = [head]
        # while nodes[-1]:
        #     nodes.append(nodes[-1].next)
        # nodes.pop()
        # return nodes[len(nodes) // 2]

        # Solution 3:
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
