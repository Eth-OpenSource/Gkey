class AmharicFSM:
    def __init__(self, rules):
        self.rules = rules
        self.buffer = ""
        self.output_stream = []
        
        # Pre-compute all valid prefixes from our rules for O(1) lookups
        self.prefixes = set()
        for key in rules.keys():
            for i in range(1, len(key) + 1):
                self.prefixes.add(key[:i])

    def process_keystroke(self, char):
        new_buffer = self.buffer + char
        
        # Longest-match rule: If adding this char still forms a valid prefix, buffer it.
        if new_buffer in self.prefixes:
            self.buffer = new_buffer
            print(f"Internal: '{new_buffer}' → pending")
            return
        
        # If new_buffer is NOT a prefix, the previous buffer reached its maximum length.
        if self.buffer in self.rules:
            emitted_char = self.rules[self.buffer]
            self.output_stream.append(emitted_char)
            print(f"Internal: '{new_buffer}' breaks prefix. Emitting '{emitted_char}' for '{self.buffer}'")
            
            # Start a fresh buffer with the new character that broke the prefix
            self.buffer = char
            print(f"Internal: '{self.buffer}' → pending")
        else:
            # Fallback for unrecognized characters (like spaces or punctuation)
            if self.buffer:
                self.output_stream.append(self.buffer)
            self.output_stream.append(char)
            self.buffer = ""
            print(f"Internal: Unrecognized char '{char}' bypassed.")

    def flush(self):
        # End of word/stream: force the remaining buffer to resolve
        if self.buffer in self.rules:
            emitted_char = self.rules[self.buffer]
            self.output_stream.append(emitted_char)
            print(f"Internal: Stream ended. Flushing '{self.buffer}' → '{emitted_char}'")
        elif self.buffer:
            self.output_stream.append(self.buffer)
        
        self.buffer = ""

    def get_final_output(self):
        return "".join(self.output_stream)


if __name__ == "__main__":
    # Define our lexical rules dictionary
    LEXICAL_RULES = {
        's': 'ስ', 'sa': 'ሳ', 'se': 'ሰ', 'si': 'ሲ', 'so': 'ሶ', 'su': 'ሱ', 'sie': 'ሴ',
        'h': 'ህ', 'ha': 'ሀ', 'he': 'ኸ', 'hi': 'ሂ', 'ho': 'ሆ', 'hu': 'ሁ', 'hie': 'ሄ',
        'sh': 'ሽ', 'sha': 'ሻ', 'she': 'ሸ', 'shi': 'ሺ', 'sho': 'ሾ', 'shu': 'ሹ',
        'l': 'ል', 'la': 'ላ', 'le': 'ለ', 'li': 'ሊ', 'lo': 'ሎ', 'lu': 'ሉ',
        'm': 'ም', 'ma': 'ማ', 'me': 'መ', 'mi': 'ሚ', 'mo': 'ሞ', 'mu': 'ሙ',
    }

    engine = AmharicFSM(LEXICAL_RULES)
    
    input_word = "selam"
    print(f"Input stream: '{input_word}'\n" + "-"*30)
    
    # Simulate user typing one character at a time
    for stroke in input_word:
        engine.process_keystroke(stroke)
        
    engine.flush()
    
    print("-"*30)
    print(f"Final Output: {engine.get_final_output()}")