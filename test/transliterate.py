import sys
import unicodedata

# 1. The Mapping Dictionary
# This maps Latin phonetic strings to Ethiopic Unicode characters.
# A full engine would load thousands of these from a JSON or Trie structure.
ETHIOPIC_MAP = {
    # L series
    'le': 'ለ', 'lu': 'ሉ', 'li': 'ሊ', 'la': 'ላ', 'lie': 'ሌ', 'l': 'ል', 'lo': 'ሎ',
    # M series
    'me': 'መ', 'mu': 'ሙ', 'mi': 'ሚ', 'ma': 'ማ', 'mie': 'ሜ', 'm': 'ም', 'mo': 'ሞ',
    # S series
    'se': 'ሰ', 'su': 'ሱ', 'si': 'ሲ', 'sa': 'ሳ', 'sie': 'ሴ', 's': 'ስ', 'so': 'ሶ',
}

def transliterate(word):
    # Normalize input to ensure clean standard Latin characters
    word = unicodedata.normalize('NFC', word).lower()
    
    result = []
    i = 0
    
    # 2. Greedy Parser
    while i < len(word):
        # Try matching 3 characters (e.g., 'lie')
        if i + 2 < len(word) and word[i:i+3] in ETHIOPIC_MAP:
            result.append(ETHIOPIC_MAP[word[i:i+3]])
            i += 3
        # Try matching 2 characters (e.g., 'se', 'la')
        elif i + 1 < len(word) and word[i:i+2] in ETHIOPIC_MAP:
            result.append(ETHIOPIC_MAP[word[i:i+2]])
            i += 2
        # Try matching 1 character (e.g., 'm')
        elif word[i] in ETHIOPIC_MAP:
            result.append(ETHIOPIC_MAP[word[i]])
            i += 1
        else:
            # If no match is found, leave the character as-is
            result.append(word[i])
            i += 1
            
    return "".join(result)

if __name__ == "__main__":
    # Check if a word was provided in the command line
    if len(sys.argv) < 2:
        print("Usage: python3 amharic.py <word>")
        sys.exit(1)
    
    input_text = sys.argv[1]
    output = transliterate(input_text)
    
    # 3. Output the raw UTF-8 bytes to stdout
    print(output)
