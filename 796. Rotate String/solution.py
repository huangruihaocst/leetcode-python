class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(B) == 0:
            if len(A) == 0:
                return True
            else:
                return False
        start = B[0]
        pos = [i for i, c in enumerate(A) if c == start]
        for p in pos:
            if A[p:] + A[:p] == B:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.rotateString('cdefabab', 'abcdefab'))
