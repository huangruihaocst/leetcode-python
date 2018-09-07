class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {')': '(', ']': '[', '}': '{'}
        stack = list()
        for i in s:
            if i in {'(', '[', '{'}:
                stack.append(i)
            else:
                if not stack:
                    return False
                if stack[-1] == d[i]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


if __name__ == '__main__':
    s = Solution()
    print(s.isValid('{[]}'))
