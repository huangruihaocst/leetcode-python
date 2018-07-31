class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if val == nums[i]:
                for j in range(len(nums) - 1, i - 1, -1):
                    if j == i:
                        nums.pop()
                        break
                    else:
                        tail = nums.pop()
                        if tail != val:
                            nums[i] = tail
                            break
            i += 1
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    n = [0, 1, 2, 2, 3, 0, 4, 2]
    print(s.removeElement(n, 2))
    print(n)
