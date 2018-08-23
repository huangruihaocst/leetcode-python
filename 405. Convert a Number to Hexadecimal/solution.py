class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        def to_hex(n):
            assert n > 0
            res = list()
            while n > 15:
                res.append(n % 16)
                n //= 16
            res.append(n)
            d = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
            return map(lambda i: str(i) if i < 10 else d[i], res[::-1])

        if num == 0:
            return '0'
        elif num > 0:
            return ''.join(to_hex(num))
        else:
            return ''.join(to_hex(2 ** 32 + num))


if __name__ == '__main__':
    s = Solution()
    print(s.toHex(-1))
