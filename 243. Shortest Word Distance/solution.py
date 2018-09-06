class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        prev1, prev2 = -1, -1
        res = float('inf')
        for index, word in enumerate(words):
            if word == word1:
                prev1 = index
                if prev2 > -1:
                    res = min(res, index - prev2)
            elif word == word2:
                prev2 = index
                if prev1 > -1:
                    res = min(res, index - prev1)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'coding', 'practice'))
