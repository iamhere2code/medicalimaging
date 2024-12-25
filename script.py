# Importing the OpenCV library
import cv2
# Reading the image using imread() function
image = cv2.imread('images/nine_dogs.jpg')   
output = image.copy()

# Using the rectangle() function to create a rectangle.
text = cv2.putText(output, 'OpenCV Demo', (500, 550),
                cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 2)