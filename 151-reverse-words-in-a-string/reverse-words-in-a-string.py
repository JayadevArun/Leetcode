class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        s=s[::-1]
        words=s.split()
        for i in range(len(words)):
            words[i]=words[i][::-1]
        return ' '.join(words)