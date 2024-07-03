class Solution:
    def isHappy(self, n: int) -> bool:

        s=set()
        
        while n!=1:
            if(n in s):
                return False
            s.add(n)

            sum=0
            while n>0:
                digit=n%10
                sum+=digit*digit
                n=n//10
            n=sum
        
        return True