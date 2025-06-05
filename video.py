import cv2
from picamera2 import Picamera2
import libcamera
import time 

print("Initializing camera...")
picam2 = Picamera2()

print("Configuring camera...")
# size (640, 480)
frame_width = 1920 
frame_height = 1080


config = picam2.create_preview_configuration(main={"format": 'RGB888', "size": (frame_width, frame_height)})
config["transform"] = libcamera.Transform(hflip=1, vflip=1)
picam2.configure(config)

print("Starting camera...")
picam2.start()

# Optional: Give the camera some time to adjust settings like exposure
time.sleep(1)

print("Displaying camera feed in OpenCV window.")
print("Press 'q' in the window to quit.")

# Create an OpenCV window
cv2.namedWindow("Camera Feed", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("Camera Feed", 1280, 960) # Optional: Resize window if needed


output_filename = 'output_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
fps = 20.0
video_writer = cv2.VideoWriter(output_filename, fourcc, fps, (frame_width, frame_height))

try:
    while True:
        # 1. Capture a frame from the camera as a NumPy array.
        # capture_array() typically returns an RGB image with default configs.
        frame_rgb = picam2.capture_array()

        # 2. Convert the frame from RGB (Picamera2 format) to BGR (OpenCV format).
        frame_bgr = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)

        if video_writer.isOpened():
            video_writer.write(frame_bgr)

        # 3. Display the frame in the OpenCV window.
        cv2.imshow("Camera Feed", frame_bgr)

        # 4. Wait for a key press for 1 millisecond.
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print("Quit key ('q') pressed.")
            break


finally:
    # --- Cleanup ---
    # This block runs even if errors occur or Ctrl+C is pressed (though waitKey catches 'q')
    print("Stopping camera and closing resources...")
    picam2.stop()             # Stop the camera stream

    if 'video_writer' in locals() and video_writer.isOpened(): # Check if video_writer was initialized and opened
        print(f"Releasing video writer for {output_filename}...")
        video_writer.release()

    cv2.destroyAllWindows() 


print("Script finished.")