import evdev
import sys

# 1. Search /dev/input for devices
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
keyboard = None

# 2. Find the first device that acts like a keyboard (has an ENTER key)
for device in devices:
    if evdev.ecodes.EV_KEY in device.capabilities():
        if evdev.ecodes.KEY_ENTER in device.capabilities()[evdev.ecodes.EV_KEY]:
            keyboard = device
            break

if not keyboard:
    print("No keyboard found. Are you running this with sudo?")
    sys.exit(1)

print(f"Hooked directly into hardware: {keyboard.name} at {keyboard.path}")
print("Press some keys! (Press Ctrl+C to exit)\n")

# 3. Read raw kernel events in an infinite loop
try:
    for event in keyboard.read_loop():
        # Only process key events (ignore mouse movements, etc.)
        if event.type == evdev.ecodes.EV_KEY:
            key_event = evdev.categorize(event)
            # Only print when the key is pressed down
            if key_event.keystate == key_event.key_down:
                print(f"Kernel detected: {key_event.keycode}")
except KeyboardInterrupt:
    print("\nExiting...")
