class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = list()
        vowels = 'aeiouAEIOU'
        for index, word in enumerate(S.split(' ')):
            if word[0] in vowels:
                new = word + 'ma'
            else:
                new = word[1:] + word[0] + 'ma'
            new += 'a' * (index + 1)
            res.append(new)
        return ' '.join(res)

if __name__ == '__main__':
    s = Solution()
    print(s.toGoatLatin('The quick brown fox jumped over the lazy dog'))
