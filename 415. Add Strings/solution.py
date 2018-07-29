class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        li = list()
        while i >= 0 or j >= 0:
            curr = carry
            if i >= 0:
                curr += int(num1[i])
            if j >= 0:
                curr += int(num2[j])
            if curr > 9:
                carry = 1
                li.append(str(curr - 10))
            else:
                carry = 0
                li.append(str(curr))
            i -= 1
            j -= 1
        if carry > 0:
            li.append('1')
        return ''.join(li[::-1])


if __name__ == '__main__':
    s = Solution()
    print(s.addStrings('1233294', '142423'))
