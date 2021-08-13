from PIL import Image

DATA = "../../data/"


# read an image and examine some basic attributes using the Image class
def image_info(file):
    image = Image.open(file)
    print("Filename:", image.filename)
    print("Format", image.format)
    print("Mode:", image.mode)
    print("Size:", image.size)
    print(f"Width={image.width} Height={image.height}")

    # image.info is a dictionary of related data (Exif, ...)
    print('--- image.info ---')
    for k, v in image.info.items():
        print(f"{k}: {v}")


if __name__ == '__main__':
    image_info(DATA + "green_hills.jpg")
