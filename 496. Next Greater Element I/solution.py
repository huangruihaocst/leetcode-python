class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Solution 1: Brute Force, O(n ^ 2)
        # res = list()
        # for i in nums1:
        #     start = nums2.index(i)
        #     found = False
        #     for n in nums2[start + 1:]:
        #         if n > i:
        #             res.append(n)
        #             found = True
        #             break
        #     if not found:
        #         res.append(-1)
        # return res

        # Solution 2: Stack, O(n)
        stack = list()
        d = dict()
        for i in nums2[::-1]:
            if len(stack) == 0:
                d[i] = -1
            else:
                while len(stack) > 0 and stack[-1] < i:
                    stack.pop()
                if len(stack) == 0:
                    d[i] = -1
                else:
                    d[i] = stack[-1]
            stack.append(i)

        res = list()
        for i in nums1:
            res.append(d[i])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
