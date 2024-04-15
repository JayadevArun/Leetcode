class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = -1
        for i,value in enumerate(word):
            if value == ch:
                index = i
                break
        if index == -1:
            return word
        rev = word[:index+1]
        rev = rev[::-1]
        rem = word[index+1:]
        res = rev + rem
        return ''.join(res)