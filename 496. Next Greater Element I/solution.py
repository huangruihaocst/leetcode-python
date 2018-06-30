class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = list()
        for i in nums1:
            start = nums2.index(i)
            found = False
            for n in nums2[start + 1:]:
                if n > i:
                    res.append(n)
                    found = True
                    break
            if not found:
                res.append(-1)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.nextGreaterElement([2,4], [1,2,3,4]))
