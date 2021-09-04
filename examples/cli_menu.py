menu = {
    "A": ("Action A", "action_a"),
    "B": ("Action B", "action_b"),
    "C": ("Action C", "action_c"),
    "Q": ("Quit", "quit_menu"),
}


def do_menu():
    while True:
        print()
        for k, v in menu.items():
            print(f"{k}) {v[0]}")

        reply = input("Select an action or Q to quit > ").upper()
        print()
        if len(reply) != 1:
            print("Input too long or empty")
            continue
        if reply not in menu:
            print("Invalid response")
            continue

        dispatch(menu[reply][1])


def quit_menu():
    print("Quitting")
    quit(0)


def action_a():
    print("*** AAA ***")


def action_b():
    print("*** BBB ***")


def action_c():
    print("*** CCC ***")


def dispatch(action_name):
    action = globals().get(action_name)
    if callable(action):
        action()


if __name__ == '__main__':
    do_menu()
