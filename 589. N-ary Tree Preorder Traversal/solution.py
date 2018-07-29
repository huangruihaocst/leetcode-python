# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = list()

        def DFS(node):
            if not node:
                return
            res.append(node.val)
            for child in node.children:
                DFS(child)

        DFS(root)
        return res
