# A simplified subset of SERA (System for Ethiopic Representation in ASCII) mappings.
# We map ASCII keystroke sequences to Ge'ez characters.
# In a full implementation, this dictionary would contain all characters.

# The structure maps sequences of characters to their Ge'ez equivalent.
# Typically, the first consonant types the 6th order character (e.g., 't' -> 'ት').
# When a vowel follows, it replaces the 6th order character with the appropriate order.

SERA_MAPPING = {
    'h': 'ህ',
    'he': 'ሀ',
    'hu': 'ሁ',
    'hi': 'ሂ',
    'ha': 'ሃ',
    'hE': 'ሄ',
    'ho': 'ሆ',

    'l': 'ል',
    'le': 'ለ',
    'lu': 'ሉ',
    'li': 'ሊ',
    'la': 'ላ',
    'lE': 'ሌ',
    'lo': 'ሎ',

    'm': 'ም',
    'me': 'መ',
    'mu': 'ሙ',
    'mi': 'ሚ',
    'ma': 'ማ',
    'mE': 'ሜ',
    'mo': 'ሞ',

    's': 'ስ',
    'se': 'ሰ',
    'su': 'ሱ',
    'si': 'ሲ',
    'sa': 'ሳ',
    'sE': 'ሴ',
    'so': 'ሶ',

    't': 'ት',
    'te': 'ተ',
    'tu': 'ቱ',
    'ti': 'ቲ',
    'ta': 'ታ',
    'tE': 'ቴ',
    'to': 'ቶ',
}
