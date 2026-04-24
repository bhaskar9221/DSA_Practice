class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for img in image:
            i,j = 0,len(img)-1

            while i<=j:
                img[i],img[j] = 1-img[j],1-img[i]
                i += 1
                j -= 1
        return image