class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Solution 1:
        # visited = dict()
        # for i, v in enumerate(numbers):
        #     if target - v in visited:
        #         return [min(visited[target - v], i) + 1, max(visited[target - v], i) + 1]
        #     visited[v] = i

        # Solution 2:
        i, j = 0, len(numbers) - 1
        while True:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            if numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
