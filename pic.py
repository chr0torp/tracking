from picamera2 import Picamera2
import time
import os


home_dir = os.path.expanduser("~") 
print("Home directory:", home_dir)
place = os.path.join(home_dir, "Desktop", "Pictures")
print("place:", place)

os.makedirs(place, exist_ok=True)



camera = Picamera2()

config = camera.create_still_configuration(main={"format": 'RGB888', "size": (640, 480)})
camera.configure(config)


full_path = os.path.join(place, "image.jpg")

print("1")
camera.start()
time.sleep(2)
print("2")
camera.capture_file(full_path)
print("3")
camera.stop()
print("Done.")