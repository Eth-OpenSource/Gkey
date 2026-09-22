import sys
import tty
import termios
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine.state_machine import KeyboardState

def get_char():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def main():
    print("Ge'ez Terminal Tester (Press 'Esc' to quit)")
    print("-" * 40)
    
    engine = KeyboardState()
    screen_buffer = []
    
    while True:
        char = get_char()
        
        if ord(char) == 27:
            print("\nExiting...")
            break
            
        if ord(char) == 127 or ord(char) == 8:
            continue
            
        delete_count, insert_string = engine.process_key(char)
        
        if delete_count > 0:
            screen_buffer = screen_buffer[:-delete_count]
            
        screen_buffer.append(insert_string)
        
        screen_text = "".join(screen_buffer)
        print(f"\r{screen_text}\033[K", end="", flush=True)

if __name__ == "__main__":
    main()
