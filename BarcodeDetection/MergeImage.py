import cv2

# read two images
src1 = cv2.imread('imgs/cat.png', cv2.IMREAD_COLOR)
src1_size= src1.shape
print(src1_size)
src2 = cv2.imread('imgs/cat_mask.png', cv2.IMREAD_COLOR)

# add or blend the images
dst = cv2.addWeighted(src1,1, src2, 1, 0.0)
cv2.imwrite('Cat_merged.png', dst)
# save the output image
# cv2.imshow('Merged',dst)
# cv2.waitKey(0)