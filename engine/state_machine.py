from engine.trie import Trie
from engine.sera_rules import SERA_MAPPING

class KeyboardState:
    """
    This is the "Brain" of the keyboard while you are typing.
    It remembers what you just typed and talks to the Trie to figure out what to do.
    """
    def __init__(self):
        # 1. Setup the Trie and load all our rules into it.
        self.trie = Trie()
        for sequence, geez_char in SERA_MAPPING.items():
            self.trie.insert(sequence, geez_char)
            
        # 2. The "Memory". This string keeps track of the current letters being typed.
        # If you type 't', it becomes 't'. If you then type 'e', it becomes 'te'.
        self.current_sequence = ""

    def process_key(self, key):
        """
        This function is called every single time the user presses a key on their physical keyboard.
        It returns two things:
        1. How many characters to DELETE from the screen (backspace)
        2. What new character to INSERT onto the screen
        """
        # (We will write the logic for this function next!)
        pass
