# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        # Solution 1: BFS
        # def leaves(root):
        #     if not root:
        #         return list()
        #     visit = [root]
        #     while True:
        #         new = list()
        #         for node in visit:
        #             if node.left:
        #                 new.append(node.left)
        #             if node.right:
        #                 new.append(node.right)
        #             if not node.left and not node.right:
        #                 new.append(node)
        #         if new == visit:
        #             break
        #         else:
        #             visit = new
        #     return [node.val for node in visit]
        #
        # return leaves(root1) == leaves(root2)

        # Solution 2: DFS with yield
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)

        return list(dfs(root1)) == list(dfs(root2))


if __name__ == '__main__':
    s = Solution()
    t = TreeNode(3)
    t.left = TreeNode(5)
    t.right = TreeNode(1)
    t.left.left = TreeNode(6)
    t.left.right = TreeNode(2)
    t.right.left = TreeNode(9)
    t.right.right = TreeNode(8)
    t.left.right.left = TreeNode(7)
    t.left.right.right = TreeNode(4)
    print(s.leafSimilar(t, t))
