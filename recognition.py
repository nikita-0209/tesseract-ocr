import cv2
import pytesseract
image = cv2.imread('cropped out price.jpg')

target = pytesseract.image_to_string(image, lang='eng',config='--psm 12 --oem 3')
print (target)
