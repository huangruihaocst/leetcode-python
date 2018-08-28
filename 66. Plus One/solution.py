class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        while i > -1:
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
                i -= 1
            else:
                break
        if i == -1 and digits[0] == 0:
            digits = [1] + digits
        return digits


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([9, 9, 8, 9]))
