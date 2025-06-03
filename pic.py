from picamera import PiCamera
import os

camera = PiCamera()
time.sleep(2)

place = "/Desktop/Pictures/image0"



if not os.path.exists(place):
    number = 0
    name = place + str(number) + ".jpg"
    while os.path.exists(name):
        number += 1
        name = place + str(number) + ".jpg"


camera.capture(name)
print("Done.")