import sys

from commands import CreateOrder, UpdateOrder, ShipOrder, NoCommand


def get_commands():
    commands = (CreateOrder, UpdateOrder, ShipOrder)
    return dict([cls.name, cls] for cls in commands)  # lookup table


def print_usage(commands):
    print('Usage: after_command <command> [arguments]')
    print('Commands:')
    for command in commands.values():
        print('    %s' % command.description)


def parse_command(commands, args):
    command = commands.setdefault(args[0], NoCommand)
    return command(args)


if __name__ == '__main__':
    # no Invoker, Receiver
    commands = get_commands()
    if len(sys.argv) < 2:
        print_usage(commands)
        exit()

    # Find and execute the command
    command = parse_command(commands, sys.argv[1:])
    command.execute()
