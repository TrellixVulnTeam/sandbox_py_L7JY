import os

from PIL import Image

DATA = "../../data/"
TMP = "../../tmp/"


def image_type(file):
    with Image.open(file) as im:
        print("Image type: ", im.format)


# thumbnail and save to a file
def make_thumbnail(file):
    outfile = TMP + os.path.splitext(os.path.basename(file))[0] + ".thumb.gif"
    with Image.open(file) as img:
        img.thumbnail((96, 96))
        img.save(outfile)  # detect appropriate format from the file extension
    return outfile


if __name__ == '__main__':
    thumb_fn = make_thumbnail(DATA + "green_hills.jpg")
    image_type(thumb_fn)
