class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d = {v: i for i, v in enumerate(list1)}
        min_sum = float('inf')
        choices = dict()
        for i, r in enumerate(list2):
            if r in d:
                choices[r] = d[r] + i
                min_sum = min(min_sum, d[r] + i)
        res = list()
        for r, s in choices.items():
            if s == min_sum:
                res.append(r)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"]))
