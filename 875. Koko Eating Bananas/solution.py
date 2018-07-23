class Solution:
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """

        # Binary Search

        from math import ceil

        def count_time(K):
            return sum(ceil(pile / K) for pile in piles)

        if H == len(piles):
            return max(piles)
        if H >= count_time(1):
            return 1
        small, big = 1, max(piles)
        while True:
            middle = (small + big) // 2
            if count_time(middle) > H:  # K too small
                small = middle
            else:  # K too big
                big = middle
            if big == small:
                return small
            if big - small == 1:
                if count_time(small) <= H:
                    return small
                if count_time(big) <= H:
                    return big


if __name__ == '__main__':
    s = Solution()
    print(s.minEatingSpeed([30,11,23,4,20], 6))
