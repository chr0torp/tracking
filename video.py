
from picamzero import Camera
import os

home_dir = os.environ['HOME']
cam = Camera()

cam.start_preview()
cam.record_video(f"{home_dir}/Desktop/new_video.mp4", duration=30)
cam.stop_preview()