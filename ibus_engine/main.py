import sys
import os
import gi  # type: ignore[reportMissingImports]

# We are using GObject Introspection (gi) to talk to Linux IBus
gi.require_version('IBus', '1.0')
from gi.repository import IBus, GLib  # type: ignore[reportMissingImports]

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
        # 1. We only care about key PRESSES. Ignore it when the user lifts their finger.
        if state & IBus.ModifierType.RELEASE_MASK:
            return False
            
        # 2. Safety check: If the user presses Backspace, we need to clear our engine's 
        # memory so it doesn't accidentally combine old letters!
        if keyval == IBus.KEY_BackSpace:
            self.state_machine.current_sequence = ""
            return False # Return False so the OS handles the actual deleting

        # 3. Convert the Linux key ID into a normal string character (like 't' or 'e')
        char = IBus.keyval_to_unicode(keyval)
        
        # If it's a special key (like Enter, Shift, F1), let the OS handle it normally.
        if not char or char == '\0':
            self.state_machine.current_sequence = ""
            return False

        # 4. Pass the character to our awesome engine!
        delete_count, insert_string = self.state_machine.process_key(char)
        
        # 5. Tell the Linux OS to delete characters behind the cursor (if needed)
        if delete_count > 0:
            # -delete_count means "go backward from the cursor"
            self.delete_surrounding_text(-delete_count, delete_count)
            
        # 6. Tell the Linux OS to type the new Ge'ez character
        if insert_string:
            text = IBus.Text.new_from_string(insert_string)
            self.commit_text(text)
            
        # Return True to tell Linux: "We handled this key, don't type the English letter!"
        return True

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
