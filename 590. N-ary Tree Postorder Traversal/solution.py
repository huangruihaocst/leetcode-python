# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # Solution 1: Recursive
        # res = list()
        #
        # def DFS(node):
        #     if not node:
        #         return
        #     nonlocal res
        #     for child in node.children:
        #         DFS(child)
        #     res.append(node.val)
        #
        # DFS(root)
        # return res

        # Solution 2: Iterative
        if not root:
            return list()
        stack = [root]
        res = list()

        while stack:
            node = stack.pop()
            res.append(node.val)
            for child in node.children:
                stack.append(child)
        return res.reverse()
