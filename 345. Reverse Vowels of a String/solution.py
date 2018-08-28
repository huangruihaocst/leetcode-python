class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Solution 1:
        # vowels = list()
        # for c in s:
        #     if c in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}:
        #         vowels.append(c)
        # i = len(vowels) - 1
        # new = list()
        # for c in s:
        #     if c not in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}:
        #         new.append(c)
        #     else:
        #         new.append(vowels[i])
        #         i -= 1
        # return ''.join(new)

        # Solution 2:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        li = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if li[left] in vowels and li[right] in vowels:
                li[left], li[right] = li[right], li[left]
                left += 1
                right -= 1
            elif li[left] in vowels:
                right -= 1
            elif li[right] in vowels:
                left += 1
            else:
                left += 1
                right -= 1
        return ''.join(li)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseVowels('aA'))
