class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words=s.split()

        if len(pattern)!=len(words):
            return False

        hm={}
        ss=set()

        for letter,word in zip(pattern,words):
            if letter in hm:
                if hm[letter]!=word:
                    return False
            else:
                if word not in ss:
                    hm[letter]=word
                    ss.add(word)
                else:
                    return False
                    
        return True