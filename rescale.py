"""
Rescales the image or video input
"""
import cv2 as cv

# img = cv.imread('Sample/f6797777cdb57641f748544e7140bfd8.jpg')
# cv.imshow('Butterfly', img)

def rescale_frame(input_frame, scale=0.75):
    """
    Rescales the given image frame by a specified scaling factor.
    Iamges, Videos and Live Videos
    Parameters:
      input_frame (numpy.ndarray): The image frame to be resized.
      scale (float, optional): The scaling factor for resizing the frame. 
        Default is 0.75.
    """
    width = int(input_frame.shape[1] * scale)
    height = int(input_frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(input_frame, dimensions, interpolation=cv.INTER_AREA)


def change_res(width, height):
    """
    Live video
    """
    capture.set(3, width)
    capture.set(4, height)

capture = cv.VideoCapture('/mnt/d/Videos/CCC.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescale_frame(frame,0.5)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
