class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        c=0
        for item in patterns:
            if item in word:
                c+=1
        return c