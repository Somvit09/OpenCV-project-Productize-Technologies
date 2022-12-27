import cv2
b = cv2.imread('output.jpg')
input_image_path = 'TEST IMAGES/2.jpg'
image = cv2.imread(input_image_path)
output_gray = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(output_gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
final_output = cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
cv2.imshow('sample', final_output)
cv2.waitKey(0)
cv2.destroyAllWindows()