class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i] = image[i][::-1]
            for j in range(len(image[i])):
                image[i][j] = 1 - image[i][j]
        return image

        # for item in image:
        #     item.reverse()
        #     for i in range(len(item)):
        #         item[i]=1-item[i]
        # return image