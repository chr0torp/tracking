from picamera2 import Picamera2
import time
import os

camera = Picamera2()
time.sleep(2)

place = "/Desktop/Pictures/image0"

camera.capture_file(place + ".jpg")

# if not os.path.exists(place):
#     number = 0
#     name = place + str(number) + ".jpg"
#     while os.path.exists(name):
#         number += 1
#         name = place + str(number) + ".jpg"

print("Done.")