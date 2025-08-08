from PIL import Image

#encode bits in image
def encode_image(image_path, bits):

  img = Image.open(image_path)
  img = img.convert("RGB")
  pixels = img.load()

  width, height = img.size
  bit_index = 0
  total_bits = len(bits)

  for y in range(height):
    for x in range(width):
      if bit_index >= total_bits:
          break

      r, g, b = pixels[x, y]

      if bit_index < total_bits:
        r = (r & ~1) | int(bits[bit_index])
        bit_index += 1

      if bit_index < total_bits:
        g = (g & ~1) | int(bits[bit_index])
        bit_index += 1

      if bit_index < total_bits:
        b = (b & ~1) | int(bits[bit_index])
        bit_index += 1

      pixels[x, y] = (r, g, b)

    if bit_index >= total_bits:
      break

  img.save("encoded_image.png")

#decode bits from image
def decode_image(image_path, delimiter="1111111111111110"):
  img = Image.open(image_path)
  img = img.convert("RGB")
  pixels = img.load()

  width, height = img.size
  bits = ""

  for y in range(height):
    for x in range(width):
      r, g, b = pixels[x, y]
      bits += bin(r)[-1]
      if bits.endswith(delimiter):
        return bits[:-len(delimiter)]

      bits += bin(g)[-1]
      if bits.endswith(delimiter):
        return bits[:-len(delimiter)]

      bits += bin(b)[-1]
      if bits.endswith(delimiter):
        return bits[:-len(delimiter)]

  return bits