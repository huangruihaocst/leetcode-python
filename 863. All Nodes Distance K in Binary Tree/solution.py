# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[TreeNode]
        """
        # Solution 1:
        # parent = dict()
        # parent[root.val] = None
        # 
        # def find_parent(node):
        #     nonlocal parent
        #     if node.left is not None:
        #         parent[node.left.val] = node
        #         find_parent(node.left)
        #     if node.right is not None:
        #         parent[node.right.val] = node
        #         find_parent(node.right)
        # 
        # find_parent(root)
        # 
        # dist = 0
        # level = [target]
        # past = {target}
        # while dist < K:
        #     new = list()
        #     for node in level:
        #         if node.left is not None and node.left not in past:
        #             new.append(node.left)
        #             past.add(node.left)
        #         if node.right is not None and node.right not in past:
        #             new.append(node.right)
        #             past.add(node.right)
        #         if parent[node.val] is not None and parent[node.val] not in past:
        #             new.append(parent[node.val])
        #             past.add(parent[node.val])
        #     level = new
        #     dist += 1
        # return [node.val for node in level]
        
        # Solution 2:
        res = list()
        def subtree(node, dist):  # add nodes that are distance dist from node rooted at node
            if node is None:
                return
            if dist == 0:
                res.append(node.val)
            else:
                subtree(node.left, dist - 1)
                subtree(node.right, dist - 1)

        def DFS(node):  # return the distance from node to target, only downward allows
            if node is None:
                return -1
            elif node is target:
                subtree(target, K)
                return 0
            else:
                l, r = DFS(node.left), DFS(node.right)
                if l != -1:
                    if K == l + 1:
                        res.append(node.val)
                    else:
                        subtree(node.right, K - l - 2)
                    return l + 1
                elif r != -1:
                    if K == r + 1:
                        res.append(node.val)
                    else:
                        subtree(node.left, K - r - 2)
                    return r + 1
                else:
                    return -1
                    
        DFS(root)
        return res
            
        
if __name__ == '__main__':
    s = Solution()
    t = TreeNode(0)
    t.left = TreeNode(1)
    t.left.left = TreeNode(3)
    t.left.right = TreeNode(2)
    print(s.distanceK(t, t.left.right, 1))
