import idc

rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))
 
# Rotate right: 0b1001 --> 0b1100
ror = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))
 
max_bits = 32  # For fun, try 2, 17 or other arbitrary (positive!) values

def decrypt_strings(encrypted, decrypted):
    b = []
    out = ""
    Dword(encrypted)
    len = Word(encrypted) ^ Word(encrypted+4)
    key = Dword(encrypted)
    print "Length" + hex(len)
    starting_byte = encrypted+6
    for i in range(starting_byte, starting_byte+len):
        key = rotate(key)
        #print hex(key)
        decrypted = key ^ Dword(i)
        b.append(chr(decrypted & 0xff))
        out = ''.join(str(e) for e in b)
    return out
    
def rotate(a):
    a = a+0x2e59
    a = ror(a, 1, 32)
    a = ror(a, 1, 32)
    a = ror(a, 2, 32)
    a = a ^ 0x151d
    a = rol(a, 2, 32)
    a = rol(a, 1, 32)
    return a
    
decrypt_strings(0x19E34A0, 2)