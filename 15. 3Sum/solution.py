class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        def find_sum(left, right, _sum):
            _res = list()
            while left < right:
                if nums[left] + nums[right] == _sum:
                    _res.append([nums[left], nums[right]])
                    while left < len(nums) - 1 and nums[left + 1] == nums[left]:
                        left += 1
                    while right > 0 and nums[right - 1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < _sum:
                    left += 1
                else:
                    right -= 1
            return _res

        res = list()
        for i, v in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            others = find_sum(i + 1, len(nums) - 1, -v)
            for other in others:
                other.append(v)
                res.append(other)

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
