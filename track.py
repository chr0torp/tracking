import cv2

tracker = cv2.TrackerCSRT_create()

video_path = 'video.mp4'
video = cv2.VideoCapture(video_path)
if not video.isOpened():
    print("Error opening video file")
    exit()

ok, frame = video.read()
if not ok:
    print("Error reading video file")
    exit()

