# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        visited = dict()

        def find(val):
            nonlocal visited

            node = root
            while node:
                visited[node.val] = True
                if node.val == val:
                    return True
                elif node.val > val:
                    node = node.left
                elif node.val < val:
                    node = node.right

            return False

        def DFS(node):
            if not node:
                return False
            if k - node.val == node.val:
                return DFS(node.left) or DFS(node.right)
            nonlocal visited
            while node:
                if k - node.val in visited:
                    return True
                elif find(k - node.val):
                    return True
                else:
                    return DFS(node.left) or DFS(node.right)
            return False

        return DFS(root)


if __name__ == '__main__':
    s = Solution()
    t = TreeNode(2)
    t.left = TreeNode(1)
    t.right = TreeNode(3)
    print(s.findTarget(t, 4))
