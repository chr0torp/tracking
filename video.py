
from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
import time
import os
import signal

home_dir = os.environ.get('HOME', '/home/pi') # Provide default if HOME not set
video_path = f"{home_dir}/Desktop/new_video.mp4"
record_duration = 30 

# Initialize the camera
picam2 = Picamera2()


config = picam2.create_video_configuration()
picam2.configure(config)

# Start the preview (optional, requires a display connected or X11 forwarding)
# Choose one preview method: QTGL (requires desktop), DRMKMS (requires direct display)
# If running headless, you might skip the preview entirely.

try:
    while True:

        try:
            # Check if DISPLAY environment variable is set for QTGL preview
            display_env = os.environ.get('DISPLAY')
            if display_env:
                print("Starting QTGL preview...")
                picam2.start_preview(Preview.QTGL)
                started_preview = True

            else: 
                exit(0) 
            
            if started_preview:
                print("Preview started successfully.")
                signal.pause()
                
        except Exception as e:
            print(f"Could not start preview: {e}. Continuing without preview.")

        # encoder = H264Encoder(bitrate=10000000)
# print(f"Starting video recording for {record_duration} seconds...")
# picam2.start_recording(encoder=encoder, output=video_path)

# time.sleep(record_duration)

# picam2.stop_recording()
# print(f"Video recording stopped. Saved to {video_path}")
except KeyboardInterrupt:
    print("Recording interrupted by user.")
finally:
    # Stop the preview if it was started
    try:
        picam2.stop_preview()
    except Exception as e:
        print(f"Error stopping preview: {e}")


print("Script finished.")