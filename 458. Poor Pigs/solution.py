class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        from math import log, ceil
        times = minutesToTest // minutesToDie
        return int(ceil(log(buckets, times + 1)))


if __name__ == '__main__':
    s = Solution()
    print(s.poorPigs(1000, 15, 60))
