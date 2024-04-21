class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for item in image:
            item.reverse()
            for i in range(len(item)):
                item[i]=1-item[i]
        return image