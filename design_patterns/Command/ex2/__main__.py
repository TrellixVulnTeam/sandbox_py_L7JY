from actions import Appliance, Door, Security

from commands import (ApplianceOnCommand, ApplianceOffCommand,
                      DoorLockCommand, DoorUnlockCommand,
                      SecurityArmCommand, SecurityDisarmCommand)
from menu_action import MenuAction

if __name__ == '__main__':
    # instantiate new objects
    menu_action = MenuAction()  # Invoker
    frontdoor = Door('Front Door')
    frontdoor_lock = DoorLockCommand(frontdoor)
    frontdoor_unlock = DoorUnlockCommand(frontdoor)

    # Set up the commands
    menu_action.set_command(frontdoor, frontdoor_lock, frontdoor_unlock)

    # Try the commands with undo
    menu_action.activate(frontdoor)
    menu_action.deactivate(frontdoor)
    menu_action.deactivate(frontdoor)
    menu_action.undo()
    menu_action.undo()
    menu_action.undo()

    # Extra undo to test empty queue
    menu_action.undo()
