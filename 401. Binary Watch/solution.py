class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = list()
        from itertools import permutations, product
        for up in range(5):
            down = num - up
            if down < 0 or down > 6:
                continue
            hours, minutes = list(), list()
            h = [1, 2, 4, 8]
            m = [1, 2, 4, 8, 16, 32]
            h_per = set(permutations([0] * (4 - up) + [1] * up))
            for per in h_per:
                hour = sum(h[i] * per[i] for i in range(4))
                if hour <= 11:
                    hours.append(str(hour))
            m_per = set(permutations([0] * (6 - down) + [1] * down))
            for per in m_per:
                minute = sum(m[i] * per[i] for i in range(6))
                if minute <= 9:
                    minutes.append('0' + str(minute))
                elif minute <= 59:
                    minutes.append(str(minute))
            prod = product(hours, minutes)
            for t in prod:
                res.append(t[0] + ':' + t[1])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.readBinaryWatch(1))

