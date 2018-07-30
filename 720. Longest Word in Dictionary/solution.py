class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort(reverse=True)
        words.sort(key=lambda w: len(w))
        s = set(words)
        for word in words[::-1]:
            length = len(word)
            cnt = 0
            for i in range(1, length):
                if word[:-i] in s:
                    cnt += 1
            if cnt == length - 1:
                return word
        return ''


if __name__ == '__main__':
    s = Solution()
    print(s.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))

