from PIL import Image
from collections import Counter

def getPixelData(imgFile):
    try:
        img = Image.open(imgFile)
        width, height = img.size
        pixels = img.load()
        print(f"Image data:\n\
            width : {width}\n\
            height: {height}")

        print(pixels[0, 0])
        return (width, height, pixels)
                
    except FileNotFoundError:
        print("Error: image not found")

def generateGrayScale():
    colors = []
    for i in range(0, 256):
        colors.append((i, i, i))
    return colors

def validatePixel(pixel):
    c = Counter(pixel[:-1])
    value, _ = c.most_common(1)[0]
    return (value, value, value, pixel[-1])


try:
    img = Image.open("image1.png")
    width, height = img.size
    pixels = img.load()
    print(f"Image data:\n\
        width : {width}\n\
        height: {height}")

    scale = generateGrayScale()
    for y in range(height):
        for x in range(width):
            pixelValue = pixels[x, y]
            valid = validatePixel(pixelValue)
            if scale.index(validatePixel(pixelValue)[:-1]) > len(pixelValue)/2:
                pixels[x, y] = scale[0]
            else:
                pixels[x, y] = scale[-1]
    img.save("reverted.png")
            
except FileNotFoundError:
    print("Error: image not found")

