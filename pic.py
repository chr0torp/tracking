from picamera2 import Picamera2
import time
import os


home_dir = os.path.expanduser("~") 
print("Home directory:", home_dir)
place = os.path.join(home_dir, "Desktop", "Pictures")
print("place:", place)

os.makedirs(place, exist_ok=True)

camera = Picamera2()
time.sleep(2)

full_path = os.path.join(place, "image.jpg")
camera.capture_file(full_path)

camera.stop()
print("Done.")