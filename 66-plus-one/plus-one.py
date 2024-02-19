class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c=0
        b=False
        if digits[-1]==9:
            for i in range(len(digits)-1,-1,-1):
                if digits[i]==9 and b==False:
                    c+=1
                else:
                    b=True
            if c==len(digits):
                digits[len(digits)-c]=1
                for i in range(len(digits)-c+1,len(digits)):
                    digits[i]=0
                digits.append(0)
            else:
                digits[len(digits)-c-1]+=1
                for i in range(len(digits)-c,len(digits)):
                    digits[i]=0
            return digits
        else:
            digits[len(digits)-1]+=1
            return digits
