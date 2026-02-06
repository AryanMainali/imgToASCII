from PIL import Image, ImageDraw, ImageFont
import math

char = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`'. "
char_Array =list(char)
char_Array.reverse()

text_file = open("output.txt", "w")

img = Image.open("input.png")
width, height = img.size
img = img.resize((int(0.25*width), int(0.15*height)), Image.NEAREST)
width, height = img.size
pix = img.load()

def getChar(inputInt):
    return char_Array[math.floor(inputInt*(69/256))]

print(width, height)

for i in range(height):
    for j in range(width):
        r, g, b, a = pix[j, i]
        s = int((r+g+b)/3)
        pix[j, i] = (s, s, s)
        text_file.write(getChar(s))
    text_file.write("\n")