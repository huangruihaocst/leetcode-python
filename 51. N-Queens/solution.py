class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res_num = list()  # result in the form of number list

        # change a list of numbers to the answer with required format
        def to_ans(li):
            ans = list()
            for pos in li:
                ans_str = '.' * pos + 'Q' + '.' * (n - pos - 1)
                ans.append(ans_str)
            return ans

        def check(curr, pos):  # check if it is legal to put a new queen on position pos
            if len(curr) == 0:
                return True
            if pos in curr:
                return False
            if pos in (curr[-1] - 1, curr[-1] + 1):
                return False
            return True

        from copy import deepcopy

        def DFS(curr):
            nonlocal res_num
            print(curr)
            if len(curr) == n:
                res_num.append(deepcopy(curr))
                return
            for pos in range(0, n):
                if check(curr, pos):
                    curr.append(pos)
                    DFS(curr)
                    curr.pop()

        DFS(list())
        res_str = list()  # result in the form of string list
        for num_list in res_num:
            res_str.append(to_ans(num_list))

        return res_str


if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(4))
