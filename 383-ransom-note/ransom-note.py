class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rN=set(ransomNote)
        for i in rN:
            if magazine.count(i)<ransomNote.count(i):
                return False
        return True
