from cv2 import cv2
import time
from test import predict

cam = cv2.VideoCapture(0)

while True:
    is_error, img = cam.read()
    if not is_error:
        print('Error when grabbing frame')
        break

    cv2.imwrite('image.png', img)
    prediction = predict('image.png')
    print(prediction)
    time.sleep(10)

    