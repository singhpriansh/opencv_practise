'''
  Transformations of image
'''
import cv2 as cv
import numpy as np

img = cv.imread('Sample/a0f3841fc01b8aa11cd1deb4db5611da.jpg')
cv.imshow('Moon', img)

def translate(image, x, y):
    '''
      Translate function to translate an image
      -x --> left, -y --> up
      x --> right, y --> down
    '''
    trans_mat = np.array([[1, 0, x], [0, 1, y]], dtype=np.float32)
    dimensions = (image.shape[1], image.shape[0])
    return cv.warpAffine(image, trans_mat, dimensions)

translated = translate(img, 100, 100)
cv.imshow('Translated',translated)

def rotate(image, angle, rot_point=None):
    '''
      Rotate function to rotate image
      +angle --> clockwise
      -angle --> counterclockwise
    '''
    (height,width) = img.shape[:2]

    if rot_point is None:
        rot_point = (width//2, height//2)

    rot_mat = cv.getRotationMatrix2D(rot_point, angle, 1.0)
    return cv.warpAffine(image,rot_mat,(width,height))

rotated = rotate(img, 45)
cv.imshow('Rotated',rotated)

rotated = rotate(rotated, 45)
cv.imshow('Re-Rotated',rotated)

# Resizing image
resized = cv.resize(img, (img.shape[1]//2, img.shape[0]//2), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, 0)

'''
   0 --> vertically
   1 --> horizontally
  -1 --> both vertically and horizontally
'''

cv.imshow('Flip',flip)
cv.waitKey(5000)
cv.destroyAllWindows()
