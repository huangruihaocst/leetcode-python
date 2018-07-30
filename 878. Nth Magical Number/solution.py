class Solution:
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        # Solution 1: Binary Search
        # def lcm(a, b):
        #     def gcd(_a, _b):
        #         while _b > 0:
        #             _a, _b = _b, _a % _b
        #         return _a
        #     return a * b // gcd(a, b)
        #
        # _lcm = lcm(A, B)
        #
        # def magic(n):
        #     """
        #     Calculate the number of magic number below n (include n).
        #     :param n: n > 0
        #     :return: the number of magic number below n (include n).
        #     """
        #     nonlocal _lcm
        #     return n // A + n // B - n // _lcm
        #
        # left, right = 1, N * min(A, B)
        # while right - left > 1:
        #     middle = (left + right) // 2
        #     cnt = magic(middle)
        #     if cnt == N:
        #         break
        #     elif cnt < N:
        #         left = middle
        #     else:
        #         right = middle
        # if right - left == 1:
        #     while right % A != 0 and right % B != 0:
        #         right -= 1
        #     return right % 1000000007
        # else:
        #     middle = (left + right) // 2
        #     while middle % A != 0 and middle % B != 0:
        #         middle -= 1
        #     return middle % 1000000007

        # Solution 2: Mathematical
        from math import gcd
        lcm = A * B // gcd(A, B)
        every = lcm // A + lcm // B - 1
        q, r = N // every, N % every
        if r == 0:
            return q * lcm % 1000000007
        t1 = q * lcm + A
        t2 = q * lcm + B
        while r > 1:
            if t1 > t2:
                t2 += B
            else:
                t1 += A
            r -= 1
        return min(t1, t2) % 1000000007


if __name__ == '__main__':
    s = Solution()
    print(s.nthMagicalNumber(5, 2, 4))
