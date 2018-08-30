class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        from re import findall
        S = S.replace('-', '')
        S = S.upper()
        last = len(S) % K
        first = str()
        if last != 0:
            first = S[:last]
            S = S[last:]
            if len(S) > 0:
                first += '-'
        return first + '-'.join(findall('.' * K, S))


if __name__ == '__main__':
    s = Solution()
    print(s.licenseKeyFormatting('2-4A0r7-4k', 4))
