import sys
import os
import gi

# We are using GObject Introspection (gi) to talk to Linux IBus
gi.require_version('IBus', '1.0')
from gi.repository import IBus, GLib

# Import our core engine that we built in Step 1!
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from engine.state_machine import KeyboardState

class GeezEngine(IBus.Engine):
    """
    This class represents our keyboard service running in the background of Linux.
    IBus will create one of these every time the user switches to our keyboard.
    """
    def __init__(self):
        super().__init__()
        # Initialize the brain!
        self.state_machine = KeyboardState()

    def do_process_key_event(self, keyval, keycode, state):
        """
        IBus calls this function EVERY time a key is pressed anywhere on Linux.
        
        keyval: The ID of the key pressed (e.g., 97 for 'a', 65293 for 'Enter')
        state: Tells us if Shift, Ctrl, or Caps Lock is currently being held down.
        
        Returns True if we handled the key (Ge'ez), False if IBus should handle it normally (like Enter).
        """
        # We will write the logic to translate Linux keyvals into our engine here!
        return False

# This is the boilerplate code to start the service and keep it running forever in the background
def main():
    # 1. Connect to the Linux IBus system
    bus = IBus.Bus()
    
    # 2. Register our custom engine with the system
    factory = IBus.Factory.new(bus.get_connection())
    factory.add_engine("geez-custom", GLib.type_from_name("GeezEngine"))
    
    # 3. Start an infinite loop so the script never closes
    print("Ge'ez IBus Engine is starting in the background...")
    loop = GLib.MainLoop()
    loop.run()

if __name__ == "__main__":
    # We must tell GLib about our class before we start
    GLib.type_register(GeezEngine)
    main()
