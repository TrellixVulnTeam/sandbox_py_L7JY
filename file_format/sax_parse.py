# parse XML data using the SAX parser
# Push stream, not writable

import xml.sax


# define the ContentHandler subclass for our content
class MyContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        super().__init__()
        self.slideCount = 0
        self.itemCount = 0
        self.isInTitle = False

    # Handle startElement
    def startElement(self, tag_name, attrs):
        if tag_name == "slideshow":
            print("Slideshow title: " + attrs['title'])
        elif tag_name == "slide":
            self.slideCount += 1
        elif tag_name == "item":
            self.itemCount += 1
        elif tag_name == "title":
            self.isInTitle = True

    # Handle endElement
    def endElement(self, tag_name):
        if tag_name == "title":
            self.isInTitle = False

    # Handle text data
    def characters(self, chars):
        if self.isInTitle:
            print("Title: " + chars)

    # Handle startDocument
    def startDocument(self):
        print("About to start!")

    # Handle endDocument
    def endDocument(self):
        print("Finishing up!")


def main():
    # create a new content handler for the SAX parser
    handler = MyContentHandler()

    # call the parseString method on the XML text content
    # call the parse method on the XML file
    xml.sax.parse('../data/httpbin.xml', handler)

    # when we're done, print out some interesting results
    print("There were {0} slide elements".format(handler.slideCount))
    print("There were {0} item elements".format(handler.itemCount))


if __name__ == "__main__":
    main()
