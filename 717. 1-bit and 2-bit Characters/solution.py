class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        while len(bits) > 2:
            if bits[0] == 0:
                bits = bits[1:]
            else:
                bits = bits[2:]
        if bits == [0, 0] or bits == [0]:
            return True
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.isOneBitCharacter([0, 1, 0]))
