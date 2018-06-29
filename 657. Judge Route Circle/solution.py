class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x, y = 0, 0
        for move in moves:
            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'L':
                x -= 1
            elif move == 'R':
                x += 1
        if (x, y) == (0, 0):
            return True
        else:
            return False
            
if __name__ == '__main__':
    s = Solution()
    print(s.judgeCircle("LL"))
