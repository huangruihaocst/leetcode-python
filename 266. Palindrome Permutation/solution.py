class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        from collections import Counter
        counter = Counter(s)
        cnt = 0
        for k, v in counter.items():
            if v % 2 == 1:
                cnt += 1
                if cnt > 1:
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canPermutePalindrome('carerac'))
