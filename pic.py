from picamera2 import Picamera2
import libcamera
import time
import os


home_dir = os.path.expanduser("~") 
print("Home directory:", home_dir)
place = os.path.join(home_dir, "Desktop", "Pictures")
print("place:", place)

os.makedirs(place, exist_ok=True)



camera = Picamera2()
# print(camera.sensor_modes)
# size (640, 480) ; (1640,1232) ; (1920, 1080) ; (3280, 2464)
config = camera.create_still_configuration(main={"format": 'RGB888', "size": (3280, 2464)})
config["transform"] = libcamera.Transform(hflip=1, vflip=1)
camera.configure(config)


full_path = os.path.join(place, "image_0.jpg")
num = 0

while os.path.exists(full_path):
    print(f"File already exists {full_path}")
    num += 1
    full_path = os.path.join(place, f"image_{num}.jpg")



print("Full path for saving image:", full_path)
print("1")
camera.start()
time.sleep(2)
print("2")
camera.capture_file(full_path)
print("3")
camera.stop()
print("Done.")