# Use the lxml library to parse a document in memory
# ElementTree API

from lxml import etree


def main():
    # build a doc structure using the ElementTree API
    doc = etree.parse("../data/httpbin.xml").getroot()
    print(doc.tag)

    # Access the value of an attribute
    print(doc.attrib['title'])

    # Iterate over tags
    for elem in doc.findall('slide'):
        print(elem.tag)

    slide_count = len(doc.findall("slide"))
    print("There were {0} slide elements".format(slide_count))

    # Create a new slide
    new_slide = etree.SubElement(doc, "slide")
    new_slide.text = "This is a new slide"

    # Count the number of slides
    slide_count = len(doc.findall("slide"))
    item_count = len(doc.findall(".//item"))

    print("There were {0} slide elements".format(slide_count))
    print("There were {0} item elements".format(item_count))


if __name__ == "__main__":
    main()
