class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        current, lines = 0, 1
        for c in S:
            if current + widths[ord(c) - ord('a')] > 100:
                current = widths[ord(c) - ord('a')]
                lines += 1
            else:
                current += widths[ord(c) - ord('a')]
        return [lines, current]

if __name__ == '__main__':
    s = Solution()
    print(s.numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], 
    "abcdefghijklmnopqrstuvwxyz"))
