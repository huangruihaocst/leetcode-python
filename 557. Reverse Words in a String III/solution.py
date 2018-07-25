class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(map(lambda s: s[::-1], s.split(' ')))


if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("Let's take LeetCode contest"))
