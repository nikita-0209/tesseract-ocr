import cv2
import pytesseract
image = cv2.imread('cropped out price.jpg')

#To detect only Digits:
target = pytesseract.image_to_string(image, lang='eng',config='--psm 12 --oem 3 -c tessedit_char_whitelist=0123456789')
print (target)
