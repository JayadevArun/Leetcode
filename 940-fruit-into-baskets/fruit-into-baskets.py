class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        maxi=0
        basket={}
        for right in range(len(fruits)):
            basket[fruits[right]]=basket.get(fruits[right],0)+1
            while len(basket)>2:
                basket[fruits[left]]-=1
                if basket[fruits[left]]==0:            
                    del basket[fruits[left]]
                left+=1
            maxi=max(maxi,right-left+1)
        return maxi