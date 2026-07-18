from PIL import Image, ImageOps
import sys
import os
if len(sys.argv) < 3:
    sys.exit("Too few arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]
if not input_file.lower().endswith((".jpg", ".jpeg", ".png")):
    sys.exit("File type error")

if not output_file.lower().endswith((".jpg", ".jpeg", ".png")):
    sys.exit("File type error")

if os.path.splitext(input_file)[1].lower() != os.path.splitext(output_file)[1].lower():
    sys.exit("Extension mismatch")
try:
    shirt = Image.open("shirt.png")
    photo = Image.open(input_file)
    photo = ImageOps.fit(photo, shirt.size)
    photo.paste(shirt, (0, 0), shirt)
    photo.save(output_file)
except FileNotFoundError:
    sys.exit("File not found")