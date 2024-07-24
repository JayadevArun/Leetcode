class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.split()
        revwords = words[::-1]
        revstring = ' '.join(revwords)
        
        return revstring
        