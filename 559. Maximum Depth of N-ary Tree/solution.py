# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        # Solution 1: DFS
        # if not root:
        #     return 0
        # if root.children:
        #     return 1 + max(self.maxDepth(child) for child in root.children)
        # return 1  # leaf

        # Solution 2: BFS
        if not root:
            return 0
        visit = [root]
        res = 0
        while visit:
            new = list()
            for node in visit:
                if node:
                    new += node.children
            res += 1
            visit = new
        return res
