class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Solution 1:
        # win = [False, True, True, True]
        # for i in range(4, n + 1):
        #     win.append(not win[i - 1] or not win [i - 2] or not win[i -3])
        # print(win)
        # return win[n]
        
        # Solution 2:
        return n % 4 != 0


if __name__ == '__main__':
    s = Solution()
    print(s.canWinNim(100))
