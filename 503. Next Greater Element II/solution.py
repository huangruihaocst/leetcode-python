class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = list()
        for i in nums[::-1]:
            while len(stack) > 0 and stack[-1] <= i:
                stack.pop()
            stack.append(i)
        res = list()
        for i in nums[::-1]:
            while len(stack) > 0 and stack[-1] <= i:
                stack.pop()
            if len(stack) == 0:
                res.append(-1)
            else:
                res.append(stack[-1])
            stack.append(i)
        return res[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.nextGreaterElements([1, 2, 1]))
