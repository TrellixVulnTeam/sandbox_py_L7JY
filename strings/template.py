# demonstrate template string functions

from string import Template


def demo1():
    # Usual string formatting with format()
    str1 = "You're watching '{0}' by '{1}'".format("Advanced Python", "Hoge Fuga")
    print(str1)

    # Template is less functionality but more secure than format string
    # create a template with placeholders
    templ = Template("You're watching '${title}' by '${author}'")

    # use the substitute method with keyword arguments
    str2 = templ.substitute(title="Advanced Python", author="Hoge Fuga")
    print(str2)

    # use the substitute method with a dictionary
    data = {
        "author": "Hoge Fuga",
        "title": "Advanced Python"
    }
    str3 = templ.substitute(data)
    print(str3)


def demo2():
    # Using Template strings
    the_str = "The quick brown $animal $action over the lazy dog"
    the_template = Template(the_str)
    output_str = the_template.substitute(animal="fox", action="jumped")
    print(output_str)

    args = {
        "animal": "cow",
        "action": "walked"
    }
    output_str = the_template.substitute(args)
    print(output_str)


if __name__ == "__main__":
    print("--- demo1 ---")
    demo1()
    print("\n--- demo2 ---")
    demo2()
