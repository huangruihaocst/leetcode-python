# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """

        def DFS(g, node):
            if not g:
                return None
            size = len(g)
            topLeft = [[g[i][j] for j in range(size // 2)] for i in range(size // 2)]
            topRight = [[g[i][j] for j in range(size // 2, size)] for i in range(size // 2)]
            bottomLeft = [[g[i][j] for j in range(size // 2)] for i in range(size // 2, size)]
            bottomRight = [[g[i][j] for j in range(size // 2, size)] for i in range(size // 2, size)]

            size //= 2

            s = sum(sum(i) for i in topLeft)
            if s == size * size:
                node.topLeft = Node(True, True, None, None, None, None)
            elif s == 0:
                node.topLeft = Node(False, True, None, None, None, None)
            else:
                topLeftNode = Node('*', False, None, None, None, None)
                node.topLeft = topLeftNode
                DFS(topLeft, topLeftNode)

            s = sum(sum(i) for i in topRight)
            if s == size * size:
                node.topRight = Node(True, True, None, None, None, None)
            elif s == 0:
                node.topRight = Node(False, True, None, None, None, None)
            else:
                topRightNode = Node('*', False, None, None, None, None)
                node.topRight = topRightNode
                DFS(topRight, topRightNode)

            s = sum(sum(i) for i in bottomLeft)
            if s == size * size:
                node.bottomLeft = Node(True, True, None, None, None, None)
            elif s == 0:
                node.bottomLeft = Node(False, True, None, None, None, None)
            else:
                bottomLeftNode = Node('*', False, None, None, None, None)
                node.bottomLeft = bottomLeftNode
                DFS(bottomLeft, bottomLeftNode)

            s = sum(sum(i) for i in bottomRight)
            if s == size * size:
                node.bottomRight = Node(True, True, None, None, None, None)
            elif s == 0:
                node.bottomRight = Node(False, True, None, None, None, None)
            else:
                bottomRightNode = Node('*', False, None, None, None, None)
                node.bottomRight = bottomRightNode
                DFS(bottomRight, bottomRightNode)

        s = sum(sum(i) for i in grid)
        size = len(grid)
        if s == size * size:
            return Node(True, True, None, None, None, None)
        elif s == 0:
            return Node(False, True, None, None, None, None)
        else:
            root = Node('*', False, None, None, None, None)
            DFS(grid, root)
            return root


if __name__ == '__main__':
    s = Solution()
    n = s.construct([[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],
                       [1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]])
    print(n.val)
    print(n.topLeft.val)
    print(n.topRight.val)
    print(n.bottomLeft.val)
    print(n.bottomRight.val)
    print(n.topRight.topLeft.val)
    print(n.topRight.topRight.val)
    print(n.topRight.bottomLeft.val)
    print(n.topRight.bottomRight.val)
