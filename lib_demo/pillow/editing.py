from PIL import Image, ImageDraw, ImageFont

infile = "../../data/green_hills.jpg"

# use the ImageDraw routines to modify an image
with Image.open(infile) as img:
    # create a drawing context from the image
    draw = ImageDraw.Draw(img)

    # draw two lines on the image
    draw.line((0, 0) + img.size, width=40, fill=128)
    draw.line((0, img.height, img.width, 0), width=40, fill=128)
    img.show()

# use the ImageDraw routines to modify an image
with Image.open(infile) as img:
    # create a drawing context from the image
    draw = ImageDraw.Draw(img)

    # define some drawing parameters - text and font to use
    textstr = "This is some sample text"
    # On Mac, use "Arial.ttf" - capitalize the A
    txtfont = ImageFont.truetype("arial.ttf", size=48)

    # measure the text size so we can position the string
    # right along the bottom edge of the image
    txtsize = draw.textsize(textstr, font=txtfont)
    print(txtsize)
    # The textsize function returns a tuple:
    # [0] is the length, [1] is the height of the text
    location = (img.width - txtsize[0] - 20, img.height - txtsize[1] - 10)

    # draw and show the text
    draw.text(location, textstr, (255, 255, 255), font=txtfont)
    img.show()
