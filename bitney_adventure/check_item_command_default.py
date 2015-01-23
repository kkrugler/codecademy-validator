def check_item_command(room_name, command):
    # Level - 5

    # TODO see if the command is for any of the items in the player's
    # list of items. If so, print out an appropriate message, and do
    # the action, and return True so that we know the command has been
    # handled.

    if command == "eat donut":
        if not player_has_item("donut"):
            print "You don't have anything to eat"
        else:
            # TODO you need to remove the donut from the player's list of
            # items, because they've eaten it.
            print "Yum, that was tasty!"

        # We handled the command, so return True
        return True
    else:
        # We didn't handle the command, so return False
        return False

# This is a handy utility routine that you give an item name (like "key")
# and it returns True if the user has that item, otherwise False.
def player_has_item(item_name):
    global g_player_items

    # Return true if the user has the item, otherwise false.
    return g_player_items.count(item_name) > 0

# This is a list of names of items that player has taken. It starts off
# as empty. When you take an item, it gets added to this list, and when
# you drop an item, it gets removed from this list.
g_player_items = ['key']

check_item_command('hallway', 'eat donut')
