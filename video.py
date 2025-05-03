from picamera2 import Picamera2, Preview
import os
import signal
import sys # For sys.exit

print("Initializing camera...")
picam2 = Picamera2()

print("Configuring preview mode...")
# Use preview configuration for optimal preview performance
preview_config = picam2.create_preview_configuration()
picam2.configure(preview_config)

preview_started = False # Flag to track if preview actually started

try:
    display_env = os.environ.get('DISPLAY')

    if display_env:
        print("DISPLAY environment detected. Attempting QTGL preview...")
        picam2.start_preview(Preview.QTGL)
        preview_started = True # Set flag only if start_preview succeeds
        print("Preview started successfully. Press Ctrl+C to stop.")
        # Wait indefinitely until a signal (like Ctrl+C) is received
        signal.pause()
    else:
        # Inform the user if the required environment isn't present
        print("\nError: No DISPLAY environment detected.")
        print("QTGL preview requires a graphical desktop session (e.g., GUI, VNC, SSH with X11 forwarding).")
        print("Cannot start preview. Exiting.")
        # Allow script to proceed to finally block for cleanup

except KeyboardInterrupt:
    print("\nCtrl+C detected. Stopping.")

except Exception as e:
    # Catch any other errors during setup or preview start
    print(f"\nAn unexpected error occurred: {e}")
    if not preview_started:
         print("Failed to start preview. Check camera connection and logs.")

finally:
    # This block executes whether the try block succeeded, raised an exception, or was interrupted
    print("Cleaning up resources...")
    if preview_started: # Only try to stop if we successfully started
        try:
            picam2.stop_preview()
            print("Preview stopped.")
        except Exception as e:
            # Log error if stopping fails, but continue cleanup
            print(f"Warning: Error stopping preview: {e}")

    # Always try to close the camera if it was opened
    if picam2.is_open:
        try:
            picam2.close()
            print("Camera closed.")
        except Exception as e:
            print(f"Warning: Error closing camera: {e}")

print("Script finished.")