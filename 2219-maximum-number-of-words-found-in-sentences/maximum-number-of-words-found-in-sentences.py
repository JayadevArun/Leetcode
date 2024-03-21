class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        c=0
        for sentence in sentences:
            if c<len(sentence.split()):
                c=len(sentence.split())
        return c

        # c=0
        # for sentence in sentences:
        #     l=sentence.count(" ")+1
        #     if l>c:
        #         c=l
        # return c