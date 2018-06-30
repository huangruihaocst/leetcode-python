class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c != len(nums) * len(nums[0]):
            return nums
        res = [i for row in nums for i in row]
        res = [res[i * c: (i + 1) * c] for i in range(r)]
        return res
        
if __name__ == '__main__':
    s = Solution()
    print(s.matrixReshape([[1, 2], [3, 4]], 1, 4))
