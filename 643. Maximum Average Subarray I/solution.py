class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Solution 1: TLE
        # from queue import Queue
        # q = Queue()
        # curr = 0
        # # init queue
        # for num in nums[:k]:
        #     curr += num
        #     q.put(num)
        # res = curr
        # for num in nums[k:]:
        #     curr = curr - q.get() + num
        #     q.put(num)
        #     res = max(curr, res)
        # return res / k

        # Solution 2: AC
        # sums = [0]
        # for num in nums:
        #     sums.append(sums[-1] + num)
        # res = float('-inf')
        # for i, _sum in enumerate(sums):
        #     if i < k:
        #         continue
        #     res = max(res, _sum - sums[i - k])
        # return res / k

        # Solution 3:
        curr = sum(nums[:k])
        res = curr
        for i, num in enumerate(nums):
            if i < k:
                continue
            # print(num, nums[i - k])
            curr = curr + num - nums[i - k]
            res = max(res, curr)
        return res / k


if __name__ == '__main__':
    s = Solution()
    print(s.findMaxAverage([0, 4, 0, 3, 2], 1))
