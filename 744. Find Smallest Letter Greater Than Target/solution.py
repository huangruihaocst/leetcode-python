class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if ord(target) >= ord(letters[-1]):
            return letters[0]
        for letter in letters:
            if ord(letter) > ord(target):
                return letter


if __name__ == '__main__':
    s = Solution()
    print(s.nextGreatestLetter(["c", "f", "j"], 'k'))
