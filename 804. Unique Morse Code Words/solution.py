class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', 
        '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', 
        '.--', '-..-', '-.--', '--..']
        ms = list()
        for word in words:
            m = str()
            for c in word:
                m += morse[ord(c) - ord('a')]
            ms.append(m)
        return len(set(ms))

if __name__ == '__main__':
    solution = Solution()
    print(solution.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
            	
