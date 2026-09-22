from engine.trie import Trie
from engine.sera_rules import SERA_MAPPING

class KeyboardState:
    def __init__(self):
        self.trie = Trie()
        for sequence, geez_char in SERA_MAPPING.items():
            self.trie.insert(sequence, geez_char)
            
        self.current_sequence = ""

    def process_key(self, key):
        test_sequence = self.current_sequence + key
        node = self.trie.search(test_sequence)
        
        if node is not None and node.value is not None:
            delete_count = 1 if len(self.current_sequence) > 0 else 0
            self.current_sequence = test_sequence
            return (delete_count, node.value)
        else:
            if self.current_sequence == "":
                return (0, key)
            else:
                self.current_sequence = ""
                return self.process_key(key)
