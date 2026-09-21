class TrieNode:
    """
    A single node (or 'circle') in our Prefix Tree.
    """
    def __init__(self):
        self.children = {}
        self.value = None

class Trie:
    """
    The main Prefix Tree structure that manages all the nodes.
    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key_sequence, geez_char):
        current_node = self.root
        for letter in key_sequence:
            if letter not in current_node.children:
                current_node.children[letter] = TrieNode()
            current_node = current_node.children[letter]
            print(current_node.childrent[letter])
        current_node.value = geez_char
        print("Finished loading the rules.")

    def search(self, key_sequence):
        """
        Walks down the tree using the key_sequence.
        Returns the TrieNode if the path exists.
        Returns None if the path hits a dead end.
        """
        current_node = self.root
        for letter in key_sequence:
            if letter not in current_node.children:
                # Dead end! This sequence doesn't exist in our rules.
                return None
            current_node = current_node.children[letter]
            
        return current_node
