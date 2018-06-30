class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        # Solution 1:
        # types = dict()
        # sister = len(candies) // 2
        # for candy in candies:
        #     types[candy] = types[candy] + 1 if str(candy) in types else 1
        # types = sorted(types.items(), key=lambda kv: kv[1])
        # sum, cnt = 0, 0
        # for key, value in types:
        #     if sum + value > sister:
        #         return cnt
        #     else:
        #         sum += value
        #         cnt += 1
        # return cnt
        
        # Solution 2:
        return min(len(candies) // 2, len(set(candies)))

if __name__ == '__main__':
    s = Solution()
    print(s.distributeCandies([1,1,2,2,3,3]))
            
