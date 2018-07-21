class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        letters = set(ransomNote)
        for letter in letters:
            if ransomNote.count(letter) > magazine.count(letter):
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canConstruct('aa', 'aab'))
