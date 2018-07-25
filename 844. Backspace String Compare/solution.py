class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def to_list(s):
            stack = list()
            for c in s:
                if c != '#':
                    stack.append(c)
                else:
                    try:
                        stack.pop()
                    except IndexError as e:
                        pass
            return stack

        return to_list(S) == to_list(T)


if __name__ == '__main__':
    s = Solution()
    print(s.backspaceCompare('a#c', 'b'))
