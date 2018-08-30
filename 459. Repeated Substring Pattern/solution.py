class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Solution 1:
        # from re import findall
        #
        # def try_sub(sub_length):
        #     sub = s[:sub_length]
        #     find_res = findall(sub, s)
        #     return len(find_res) * len(sub) == len(s)
        #
        # lens = [i for i, v in enumerate(s) if v == s[0] and i != 0]
        # if len(lens) == 0:
        #     return False
        # for length in lens:
        #     if len(s) % length == 0 and try_sub(length):
        #         return True
        # return False

        # Solution 2:
        return s in (s * 2)[1:-1]


if __name__ == '__main__':
    s = Solution()
    print(s.repeatedSubstringPattern('abab'))
