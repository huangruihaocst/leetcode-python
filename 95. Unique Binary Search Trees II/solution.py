# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        from functools import lru_cache

        if n == 0:
            return []
        if n == 1:
            return [TreeNode(1)]

        @lru_cache(maxsize=None)
        def generate(li):  # generate a BST from a list
            if len(li) == 0:
                return [None]
            if len(li) == 1:
                return [TreeNode(li[0])]
            res = list()
            for i, v in enumerate(li):  # val will be the root
                left = generate(li[:i])
                right = generate(li[i + 1:])
                for left_i in range(len(left)):
                    for right_i in range(len(right)):
                        root = TreeNode(v)
                        root.left = left[left_i]
                        root.right = right[right_i]
                        res.append(root)
            return res

        return generate(range(1, n + 1))


if __name__ == '__main__':
    s = Solution()
    trees = s.generateTrees(2)
    print(trees)
