"""
No Command pattern
"""


class CommandExecutor(object):

    def execute_command(self, args):
        # no flexibility
        if args[0] == "CreateOrder":
            self.create_order()
        elif args[0] == "UpdateQuantity":
            self.update_quantity(args[1])
        elif args[0] == "ShipOrder":
            self.ship_order()
        else:
            print("Unrecognized command: " + args[0])

    def create_order(self):
        print('Create Order...')

    def update_quantity(self, val):
        print(val)
        old_val = 5
        print("Database Updated")
        print("Logging updated quantity from %s to %s" % (old_val, val))

    def ship_order(self):
        print('Ship Order...')


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print('Usage: before_command <command> [arguments]')
        print('Commands:')
        print('    CreateOrder')
        print('    UpdateQuantity number')
        print('    ShipOrder')
        exit()

    executor = CommandExecutor()
    executor.execute_command(sys.argv[1:])
