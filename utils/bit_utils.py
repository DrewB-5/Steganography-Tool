#add delimiter
def add_delimiter(encrypted_token, delimiter = "1111111111111110"):
  bits = ''.join(format(byte, '08b') for byte in encrypted_token)
  bits_with_delim = bits + delimiter
  return list(bits_with_delim)

#change bits back to readable bytes
def bits_to_bytes(bitstring):
    return bytes(int(bitstring[i:i+8], 2) for i in range(0, len(bitstring), 8))