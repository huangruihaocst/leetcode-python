class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        left, right = 0, 0
        d = {s[0]: 0}
        res = 1
        while right < len(s) - 1:
            right += 1
            if s[right] in d and d[s[right]] >= left:
                save = d[s[right]] + 1
                left = save
            d[s[right]] = right
            res = max(res, right - left + 1)

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('pwwkew'))
