class Solution:
    def compress(self, chars: List[str]) -> int:

        l=len(chars)
        if l<2:
            return l

        i,j=0,0

        while i<l:
            count=1
            while i<l-1 and chars[i]==chars[i+1]:
                count+=1
                i+=1

            chars[j]=chars[i]
            j+=1

            if count>1:
                for value in str(count):
                    chars[j]=value
                    j+=1

            i+=1

        return j