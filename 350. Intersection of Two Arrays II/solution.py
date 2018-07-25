class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Solution 1:
        # res = list()
        # for i in nums1:
        #     if i in nums2:
        #         res.append(i)
        #         nums2.remove(i)
        # return res

        # Solution 2:
        # d = dict()
        # for i in nums1:
        #     d[i] = d[i] + 1 if i in d else 1
        # res = list()
        # for i in nums2:
        #     if i in d and d[i] > 0:
        #         res.append(i)
        #         d[i] -= 1
        # return res

        # Solution 3:
        nums1.sort()
        nums2.sort()

        i, j = 0, 0
        res = list()
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.intersect([1, 2, 2, 1], [2, 2]))
