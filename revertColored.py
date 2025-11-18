from PIL import Image
import argparse
parser = argparse.ArgumentParser("Revert colorful pictures")

parser.add_argument("input_file", help="The path to the input file.")
parser.add_argument("--output_file", "-of", help="Specify the output file.", default="output.png")

args = parser.parse_args()
try:
    img = Image.open(args.input_file)
    width, height = img.size
    pixels = img.load()
    print(f"Image data:\n\
        width : {width}\n\
        height: {height}")

    for y in range(height):
        for x in range(width):
            pixels[x, y] = (256 - pixels[x, y][0], 256 - pixels[x, y][1], 256 - pixels[x, y][2], pixels[x, y][3])
    img.save(args.output_file)
            
except FileNotFoundError:
    print("Error: image not found")

