# Use the XML DOM to parse a document in memory

import xml.dom.minidom


def main():
    # parse the returned content into a DOM structure
    # parse(file) or parseString(str)
    domtree = xml.dom.minidom.parse("../data/httpbin.xml")
    rootnode = domtree.documentElement

    # display some information about the content
    print("The root element is '{0}'".format(rootnode.nodeName))
    print("Title '{0}'".format(rootnode.getAttribute('title')))
    items = domtree.getElementsByTagName("item")
    print("There are {0} item tags".format(items.length))

    # manipulate the content in memory
    # create a new item tag
    new_item = domtree.createElement("item")
    # add some text to the item
    new_item.appendChild(domtree.createTextNode("New item from code"))
    # now add the item to the first slide
    first_slide = domtree.getElementsByTagName("slide")[0]
    first_slide.appendChild(new_item)

    # Now count the item tags again
    items = domtree.getElementsByTagName("item")
    print("Now there are {0} item tags".format(items.length))


if __name__ == "__main__":
    main()
