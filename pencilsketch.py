# pip install opencv-python
import cv2
#reading image
image=cv2.imread("avani.jpeg")
#converting BGR image to grayscale
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# gray_image = cv2.cvtColor(image,cv2.COLOR_GRAY2RGB)
#image inversion
inverted_image = 255 - gray_image
blurred = cv2.GaussianBlur(inverted_image, (15, 5), 0)
inverted_blurred = 255- blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=225.0)
cv2.imshow("Original Image", image)
cv2.imshow("Pencil Sketch of image", pencil_sketch)
cv2.waitKey(0)