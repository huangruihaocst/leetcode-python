# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return list()
        visit = [root]
        res = list()
        while visit:
            level, new = list(), list()
            for node in visit:
                level.append(node.val)
                if node.children:
                    new += node.children
            res.append(level)
            visit = new
        return res