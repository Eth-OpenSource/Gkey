from engine.trie import Trie
from engine.sera_rules import SERA_MAPPING

class KeyboardState:
    def __init__(self):
        self.trie = Trie()
        for sequence, geez_char in SERA_MAPPING.items():
            self.trie.insert(sequence, geez_char)
            
        self.current_sequence = ""

    def process_key(self, key):
        """
        Processes a single keystroke.
        Returns (delete_count, insert_string).
        """
        # Let's see what happens if we add this key to our memory
        test_sequence = self.current_sequence + key
        
        # Ask the Trie if this path exists
        node = self.trie.search(test_sequence)
        
        if node is not None and node.value is not None:
            # SCENARIO A & B: It's a valid Ge'ez sequence!
            
            # If our memory was empty, we didn't print anything yet, so delete 0.
            # If our memory had letters, it means we printed a 6th order character 
            # previously, and we need to delete it to make room for this new one.
            delete_count = 1 if len(self.current_sequence) > 0 else 0
            
            # Update our memory with the successful sequence
            self.current_sequence = test_sequence
            
            # Tell the OS to delete (if needed) and insert the new character
            return (delete_count, node.value)
            
        else:
            # SCENARIO C: The path DOES NOT exist. 
            
            if self.current_sequence == "":
                # If memory is already empty, this key is just a normal character 
                # (like Space, a number, or punctuation). Just print it normally.
                return (0, key)
            else:
                # Our memory had something in it, but this new key broke the sequence.
                # This means the previous Ge'ez character is officially finished!
                
                # 1. Clear the memory
                self.current_sequence = ""
                
                # 2. Treat this new key as the very first letter of a brand new character.
                # We do this by calling this exact function again! (Recursion)
                return self.process_key(key)
