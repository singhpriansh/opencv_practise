"""Video analysis"""
import cv2 as cv

capture = cv.VideoCapture('''/mnt/d/Videos/MPG.mkv''')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
