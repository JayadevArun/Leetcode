class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        hmp = {}
        hmw = {}

        for letter, word in zip(pattern, words):
            if letter in hmp:
                if hmp[letter] != word:
                    return False
            else:
                hmp[letter] = word

            if word in hmw:
                if hmw[word] != letter:
                    return False
            else:
                hmw[word] = letter

        return True