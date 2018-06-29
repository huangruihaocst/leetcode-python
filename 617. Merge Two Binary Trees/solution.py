class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None:
            return t2
        elif t2 is None:
            return t1
        else:
            root = TreeNode(t1.val + t2.val)
            left = self.mergeTrees(t1.left, t2.left)
            right = self.mergeTrees(t1.right, t2.right)
            root.left = left
            root.right = right
            return root
        
if __name__ == '__main__':
    t1 = TreeNode(1)
    t1.left = TreeNode(3)
    t1.right = TreeNode(2)
    t1.left.left = TreeNode(5)
    
    t2 = TreeNode(2)
    t2.left = TreeNode(1)
    t2.right = TreeNode(3)
    t2.left.right = TreeNode(4)
    t2.right.right = TreeNode(7)
    
    s = Solution()
    t = s.mergeTrees(t1, t2)
    print(t.val)
    print(t.left.val)
    print(t.right.val)
    print(t.left.left.val)
    print(t.left.right.val)
    print(t.right.right.val)
