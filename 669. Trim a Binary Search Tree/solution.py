# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        else:
            if root.val < L:
                root = root.right
                return self.trimBST(root, L, R)
            elif root.val > R:
                root = root.left
                return self.trimBST(root, L, R)
            else:
                root.left = self.trimBST(root.left, L, R)
                root.right = self.trimBST(root.right, L, R)
                return root
                
if __name__ == '__main__':
    s = Solution()
    t = TreeNode(3)
    t.left = TreeNode(0)
    t.left.right = TreeNode(2)
    t.left.right.left = TreeNode(1)
    t.right = TreeNode(4)
    
    t = s.trimBST(t, 1, 3)
    print(t.val)
    print(t.left.val)
    print(t.left.left.val)
