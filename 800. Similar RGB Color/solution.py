class Solution:
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        def find_similar(p):  # part is a string that has a length of 2
            valid = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
            if p[0] == p[1]:
                return p
            possible = [p[0] * 2]
            if chr(ord(p[0]) - 1) in valid:
                possible.append(chr(ord(p[0]) - 1) * 2)
            if p[0] == 'a':
                possible.append('99')
            if chr(ord(p[0]) + 1) in valid:
                possible.append(chr(ord(p[0]) + 1) * 2)
            ans = None
            _min = float('inf')
            for poss in possible:
                if abs(int(poss, 16) - int(p, 16)) < _min:
                    _min = abs(int(poss, 16) - int(p, 16))
                    ans = poss
            return ans

        parts = [color[1:3], color[3:5], color[5:7]]
        res = list()
        for part in parts:
            res.append(find_similar(part))
        return '#' + ''.join(res)


if __name__ == '__main__':
    s = Solution()
    print(s.similarRGB('#09f166'))
