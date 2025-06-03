from picamera2 import Picamera2
import time
import os


home_dir = os.path.expanduser("~") 
print("Home directory:", home_dir)
place = os.path.join(home_dir, "Desktop", "Pictures", "image0.jpg")
print("place:", place)

camera = Picamera2()
time.sleep(2)

camera.capture_file(place)


print("Done.")