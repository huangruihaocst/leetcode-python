class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1:
            return True
        if word[0].isupper():
            upper = word[1].isupper()
            for letter in word[2:]:
                if letter.isupper() is not upper:
                    return False
            return True
        else:
            for letter in word[1:]:
                if letter.isupper():
                    return False
            return True

if __name__ == '__main__':
    s = Solution()
    print(s.detectCapitalUse('Google'))
