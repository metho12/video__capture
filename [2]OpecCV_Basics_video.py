# import the required packages
import cv2

# create a video capture dataset
videoCapture = cv2.VideoCapture('SampleVideo_360x240_1mb.mp4')

# get the number of frames per second
fps = videoCapture.get(cv2.CAP_PROP_FPS)

# get the frame dimensions
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# Read the first video frame
success, frame = videoCapture.read()
while success: # Loop until there are no more frames.
    # you can apply the any kind of processing to each frame
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # show the original and processed frame
    cv2.imshow('Video frame', frame)
    cv2.imshow('Gray video frame', frame_gray)
    cv2.waitKey(0)
    success, frame = videoCapture.read()
    # you can apply the any kind of processing to each frame
