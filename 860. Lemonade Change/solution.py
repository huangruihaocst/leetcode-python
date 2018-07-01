class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        mine = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            mine[bill] += 1
            change = bill - 5
            if change == 5:
                if mine[5] > 0:
                    mine[5] -= 1
                else:
                    return False
            elif change == 15:
                if mine[5] > 0 and mine[10] > 0:
                    mine[5] -= 1
                    mine[10] -= 1
                elif mine[10] < 1 and mine [5] > 2:
                    mine[5] -= 3
                else:
                    return False
        return True
                        

if __name__ == '__main__':
    s = Solution()
    print(s.lemonadeChange([5,5,5,10,20]))
