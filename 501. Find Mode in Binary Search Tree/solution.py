# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Solution 1:
        # if not root:
        #     return list()
        # d = dict()
        # res = list()
        #
        # def DFS(node):
        #     if not node:
        #         return
        #     nonlocal d, res
        #     if res:
        #         prev = d[res[0]]
        #     d[node.val] = d[node.val] + 1 if node.val in d else 1
        #     if not res:
        #         res = [node.val]
        #     else:
        #         if d[node.val] > prev:
        #             res = [node.val]
        #         elif d[node.val] == d[res[0]] and node.val not in res:
        #             res.append(node.val)
        #     DFS(node.left)
        #     DFS(node.right)
        #
        # DFS(root)
        # return res

        # Solution 2:
        if not root:
            return list()

        curr, cnt = None, 0
        max_cnt = None

        def inorder1(node):
            if not node:
                return
            nonlocal curr, cnt, max_cnt
            inorder1(node.left)
            if curr is None:
                curr, cnt = node.val, 1
                max_cnt = cnt
            else:
                if curr == node.val:
                    cnt += 1
                else:
                    curr = node.val
                    cnt = 1
            max_cnt = max(max_cnt, cnt)
            inorder1(node.right)

        inorder1(root)

        res = set()
        curr, cnt = None, 0

        def inorder2(node):
            if not node:
                return
            nonlocal curr, cnt, res
            inorder2(node.left)
            if curr is None:
                curr, cnt = node.val, 1
            else:
                if curr == node.val:
                    cnt += 1
                else:
                    curr = node.val
                    cnt = 1
            if cnt == max_cnt:
                res.add(node.val)
            inorder2(node.right)

        inorder2(root)
        return list(res)


if __name__ == '__main__':
    s = Solution()
    t = TreeNode(5)
    t.left = TreeNode(0)
    t.right = TreeNode(7)
    t.left.left = TreeNode(0)
    t.left.right = TreeNode(0)
    t.right.left = TreeNode(6)
    t.right.right = TreeNode(8)
    print(s.findMode(t))
