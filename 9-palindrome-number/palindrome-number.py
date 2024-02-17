class Solution:
    def isPalindrome(self, x: int) -> bool:
        item=str(x)
        booleans=True
        if len(item)==1:
            return True
        for i in range(int(len(item)/2)):
            if item[i]==item[len(item)-i-1]:
                continue
            else:
                booleans=False
        return booleans


            
    