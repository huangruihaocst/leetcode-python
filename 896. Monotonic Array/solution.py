class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        increase = None
        for i in range(1, len(A)):
            if A[i] == A[i - 1]:
                continue
            elif A[i] > A[i - 1]:
                if increase is None:
                    increase = True
                if not increase:  # decrease
                    return False
            else:
                if increase is None:
                    increase = False
                if increase:  # increase
                    return False
        print(increase)
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isMonotonic([1, 3, 1]))
