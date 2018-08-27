class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = list()  # result in the form of number list

        def check(curr, pos):  # check if it is legal to put a new queen on position pos
            put = len(curr)
            if put == 0:
                return True
            if pos in curr:
                return False
            for r, p in enumerate(curr):
                if pos in (p + (put - r), p - (put - r)):
                    return False
            return True

        from copy import deepcopy

        def DFS(curr):
            nonlocal res
            if len(curr) == n:
                res.append(deepcopy(curr))
                return
            for pos in range(0, n):
                if check(curr, pos):
                    curr.append(pos)
                    DFS(curr)
                    curr.pop()

        DFS(list())
        return len(res)
