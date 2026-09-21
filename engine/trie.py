class TrieNode:
    """
    A single node (or 'circle') in our Prefix Tree.
    """
    def __init__(self):
        # A dictionary holding references to the next letters.
        # Key: The typed letter (e.g., 'a')
        # Value: The next TrieNode
        self.children = {}
        
        # The Ge'ez character that this specific path represents.
        self.value = None

class Trie:
    """
    The main Prefix Tree structure that manages all the nodes.
    """
    def __init__(self):
        # Every tree starts with a blank root node.
        # When the user starts typing, we start from here.
        self.root = TrieNode()

    def insert(self, key_sequence, geez_char):
        """
        Takes a sequence of keys (like 't', 'e') and the target character ('ተ')
        and builds a path through the nodes to store it.
        """
        # We always start walking from the root node.
        current_node = self.root
        
        # Go through each letter in the sequence (e.g., first 't', then 'e')
        for letter in key_sequence:
            # If the letter doesn't have a path yet, create a new empty node!
            if letter not in current_node.children:
                current_node.children[letter] = TrieNode()
            
            # Step forward onto that node
            current_node = current_node.children[letter]
            
        # We have reached the end of the sequence. 
        # Store the Ge'ez character in this final node.
        current_node.value = geez_char
