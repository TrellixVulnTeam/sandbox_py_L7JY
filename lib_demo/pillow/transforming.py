from PIL import Image, ImageFilter, ImageOps

infile = "../../data/green_hills.jpg"

# use the crop function to crop an image
with Image.open(infile) as img:
    # show the image using the platform viewer app
    img.show()

    # calculate the middle part
    midx = img.width // 2
    midy = img.height // 2
    croparea = (midy - 400, midx - 250, midy + 400, midx + 250)
    cropimg = img.crop(croparea)
    cropimg.show()

# perform a simple resize and rotation
with Image.open(infile) as img:
    newimg = img.resize((256, 256)).rotate(45)
    newimg.show()

# use the transpose function with a built-in operation
with Image.open(infile) as img:
    newimg = img.transpose(Image.FLIP_TOP_BOTTOM)
    newimg.show()

# Use an ImageFilter operation
with Image.open(infile) as img:
    newimg = img.filter(ImageFilter.GaussianBlur(10))
    newimg.show()

# Use ImageOps for built-in image processing
with Image.open(infile) as img:
    newimg = ImageOps.grayscale(img)
    newimg.show()
