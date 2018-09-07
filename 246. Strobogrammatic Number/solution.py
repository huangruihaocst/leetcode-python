class Solution:
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        invalid = ['2', '3', '4', '5', '7']
        for i in invalid:
            if i in num:
                return False
        reverse = num[::-1]
        d = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        new = list()
        for i in reverse:
            new.append(d[i])
        return ''.join(new) == num