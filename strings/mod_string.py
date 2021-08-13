import string


# predefined string constants can be used in common scenarios
def string_constants():
    print(string.ascii_letters)
    print(string.ascii_lowercase)
    print(string.ascii_uppercase)
    print(string.digits)
    print(string.octdigits)
    print(string.hexdigits)
    print(string.punctuation)
    print(string.whitespace)
    print(string.printable)


def template():
    # Using Template strings
    the_str = "The quick brown ${animal} ${action} over the lazy dog"

    # Template is less functionality but more secure than format string
    # create a template with placeholders
    the_template = string.Template(the_str)

    # use the substitute method with keyword arguments
    output_str = the_template.substitute(animal="fox", action="jumped")
    print(output_str)

    # use the substitute method with a dictionary
    data = {
        "animal": "cow",
        "action": "walked"
    }
    output_str = the_template.substitute(data)  # unpack not needed
    print(output_str)


if __name__ == '__main__':
    string_constants()
    print()
    template()
