class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        l = len(flowerbed)
        c = 0

        for i in range(l):
            if flowerbed[i] == 0:
                first = (i == 0) or (flowerbed[i - 1] == 0)
                last = (i == l - 1) or (flowerbed[i + 1] == 0)
                
                if first and last:
                    flowerbed[i] = 1
                    c += 1
                    if c >= n:
                        return True

        return c >= n