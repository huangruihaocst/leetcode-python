class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        occurences = [i for i in range(0, len(S)) if S[i] == C]
        small, big, j = -float('Inf'), occurences[0], 0
        res = list()
        for i in range(0, len(S)):
            current = min(abs(i - small), abs(big - i))
            res.append(current)
            if current == 0:
                small = big
                j += 1
                big = occurences[j] if j < len(occurences) else big
        return res
        
if __name__ == '__main__':
    s = Solution()
    print(s.shortestToChar('loveleetcode', 'e'))
