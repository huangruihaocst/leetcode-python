class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        lines = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        res = list()
        for word in words:
            curr = str()
            for line in lines:
                if word[0].lower() in line:
                    curr = line
                    break
            failed = False
            for c in word:
                if c.lower() not in curr:
                    failed = True
                    break
            if failed:
                continue
            res.append(word)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))
