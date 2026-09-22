SERA_MAPPING = {}

def add_family(base_key, base_hex):
    """
    Ge'ez Unicode characters are arranged in a strict order (1st to 7th).
    We use this to automatically generate all 7 combinations for a consonant.
    Unicode offsets: 0=1st(e), 1=2nd(u), 2=3rd(i), 3=4th(a), 4=5th(E), 5=6th(base), 6=7th(o)
    """
    SERA_MAPPING[base_key] = chr(base_hex + 5)
    
    SERA_MAPPING[base_key + 'e'] = chr(base_hex + 0)
    SERA_MAPPING[base_key + 'u'] = chr(base_hex + 1)
    SERA_MAPPING[base_key + 'i'] = chr(base_hex + 2)
    SERA_MAPPING[base_key + 'a'] = chr(base_hex + 3)
    SERA_MAPPING[base_key + 'E'] = chr(base_hex + 4)
    SERA_MAPPING[base_key + 'o'] = chr(base_hex + 6)

add_family('h', 0x1200)  # ሀ
add_family('l', 0x1208)  # ለ
add_family('H', 0x1210)  # ሐ
add_family('m', 0x1218)  # መ
add_family('sz', 0x1220) # ሠ
add_family('r', 0x1228)  # ረ
add_family('s', 0x1230)  # ሰ
add_family('sh', 0x1238) # ሸ
add_family('q', 0x1240)  # ቀ
add_family('b', 0x1260)  # በ
add_family('v', 0x1268)  # ቨ
add_family('t', 0x1270)  # ተ
add_family('c', 0x1278)  # ቸ
add_family('x', 0x1280)  # ኀ
add_family('n', 0x1290)  # ነ
add_family('N', 0x1298)  # ኘ
add_family('k', 0x12A8)  # ከ
add_family('K', 0x12B0)  # ኸ
add_family('w', 0x12C8)  # ወ
add_family('`', 0x12D0)  # ዐ
add_family('z', 0x12D8)  # ዘ
add_family('Z', 0x12E0)  # ዠ
add_family('y', 0x12E8)  # የ
add_family('d', 0x12F0)  # ደ
add_family('j', 0x12F8)  # ጀ
add_family('g', 0x1308)  # ገ
add_family('T', 0x1310)  # ጠ
add_family('C', 0x1318)  # ጨ
add_family('P', 0x1320)  # ጰ
add_family('S', 0x1328)  # ጸ
add_family('tz', 0x1330) # ፀ
add_family('f', 0x1338)  # ፈ
add_family('p', 0x1340)  # ፐ

# Independent Vowels (አ family)
SERA_MAPPING['e'] = chr(0x12A0) # አ 
SERA_MAPPING['u'] = chr(0x12A1) # ኡ 
SERA_MAPPING['i'] = chr(0x12A2) # ኢ 
SERA_MAPPING['a'] = chr(0x12A3) # ኣ 
SERA_MAPPING['E'] = chr(0x12A4) # ኤ 
SERA_MAPPING['I'] = chr(0x12A5) # እ 
SERA_MAPPING['o'] = chr(0x12A6) # ኦ 
