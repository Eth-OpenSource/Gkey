class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key_sequence, geez_char):
        current_node = self.root
        for letter in key_sequence:
            if letter not in current_node.children:
                current_node.children[letter] = TrieNode()
            current_node = current_node.children[letter]
        current_node.value = geez_char

    def search(self, key_sequence):
        current_node = self.root
        for letter in key_sequence:
            if letter not in current_node.children:
                return None
            current_node = current_node.children[letter]
            
        return current_node
