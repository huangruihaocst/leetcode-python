# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        visited = 0  # the sum of visited nodes

        def convert(node):
            if node:
                nonlocal visited
                if node.right:
                    convert(node.right)
                tmp = node.val
                node.val += visited
                visited += tmp
                if node.left:
                    convert(node.left)

        convert(root)
        return root


if __name__ == '__main__':
    s = Solution()
    # t = TreeNode(5)
    # t.left = TreeNode(2)
    # t.right = TreeNode(13)
    # t.right.left = TreeNode(6)
    # t.right.right = TreeNode(15)
    # t1 = s.convertBST(t)
    # print(t1.val)
    # print(t1.left.val)
    # print(t1.right.val)
    # print(t1.right.left.val)
    # print(t1.right.right.val)
    print(s.convertBST(None))
