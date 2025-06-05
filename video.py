import cv2
from picamera2 import Picamera2
import libcamera
import time 

print("Initializing camera...")
picam2 = Picamera2()

print("Configuring camera...")
# size (640, 480)
config = picam2.create_preview_configuration(main={"format": 'RGB888', "size": (1920, 1080)})
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

try:
    while True:
        # 1. Capture a frame from the camera as a NumPy array.
        # capture_array() typically returns an RGB image with default configs.
        frame_rgb = picam2.capture_array()

        # 2. Convert the frame from RGB (Picamera2 format) to BGR (OpenCV format).
        # OpenCV's imshow function expects BGR format by default.
        frame_bgr = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)

        # 3. Display the frame in the OpenCV window.
        cv2.imshow("Camera Feed", frame_bgr)

        # 4. Wait for a key press for 1 millisecond.
        # This is CRUCIAL:
        #  - It allows OpenCV to process GUI events and update the window.
        #  - It checks if the 'q' key was pressed.
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print("Quit key ('q') pressed.")
            break
        # Add other key checks here if needed (e.g., ord('s') to save)

finally:
    # --- Cleanup ---
    # This block runs even if errors occur or Ctrl+C is pressed (though waitKey catches 'q')
    print("Stopping camera and closing resources...")
    picam2.stop()             # Stop the camera stream
    cv2.destroyAllWindows()   # Close the OpenCV display window
    # picam2.close()          # Optional: close the camera object if fully done

print("Script finished.")