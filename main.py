import cv2
from rembg import remove

# setting path of the image
input_image_path = 'TEST IMAGES/1.jpg'
image = cv2.imread(input_image_path)

# after resizing the image
resized_image = cv2.resize(image, (1080, 720), interpolation=cv2.INTER_LINEAR)

# selected image
selected_image = cv2.selectROI("Select the area you want to select!", resized_image)
print(selected_image, resized_image.shape)

# Crop image
cropped_image = resized_image[int(selected_image[1]):int(selected_image[1]+selected_image[3]), int(selected_image[0]):int(selected_image[0]+selected_image[2])]

# resizing the cropped image
resized_cropped_image = cv2.resize(cropped_image, (1080, 720), interpolation=cv2.INTER_LINEAR)

# remove background from image 
output = remove(resized_cropped_image)
cv2.imwrite('output.jpg', output)

# grayscale image conversion
output_gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(output_gray, 120, 255, 0)  # finding threshold
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)  # finding contours
cropped_outlined_output = cv2.drawContours(resized_cropped_image, contours, -1, (0, 255, 0), 2)  # drawing contours / outlines 
print(resized_cropped_image.shape)
resized_image[selected_image[0]:selected_image[2], selected_image[1]:selected_image[3]] = cropped_outlined_output

cv2.imshow('sample', resized_image)
cv2.waitKey(0)

