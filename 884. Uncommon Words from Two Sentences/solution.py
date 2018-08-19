class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        from collections import Counter
        counter_a, counter_b = Counter(A.split(' ')), Counter(B.split(' '))
        res = list()
        for word, cnt in counter_a.items():
            if cnt == 1 and word not in counter_b:
                res.append(word)
        for word, cnt in counter_b.items():
            if cnt == 1 and word not in counter_a:
                res.append(word)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.uncommonFromSentences('apple apple', 'banana'))
