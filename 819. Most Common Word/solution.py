class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = paragraph.split(' ')
        import re
        words = map(lambda word: re.sub('[!?\',;.]', '', word).lower(), words)
        words = [word for word in words if word not in banned]
        from collections import Counter
        return Counter(words).most_common()[0][0]


if __name__ == '__main__':
    s = Solution()
    print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))