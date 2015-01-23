def examine_item_command(room_name, command):
    # Level - 3

    global g_player_items
    global g_game_items

    # First use the handy-dandy get_item_name utility function to extract
    # the item name from the command.
    item_name = get_item_name("examine", command)

    # TODO if item_name isn't in the player's
    # list of items, print an error message. Otherwise print
    # the item's description. You can use the player_has_item(item_name)
    # utility function to help with this.

    print "I don't know how to examine " + item_name

# This is a list of names of items that player has taken. It starts off
# as empty. When you take an item, it gets added to this list, and when
# you drop an item, it gets removed from this list.
g_player_items = ["key"]

# items is a dictionary, where the key is the item name, and the value is an "item"
# Each item is also a dictionary, where the key is one of several possible values
#   description -> string that describes the item
#   takeable -> boolean for whether the item can be taken or not.
#
# You can also have other item-specific attributed, e.g. a bottle of water could have
# an "empty": False attribute, and this changes to True after you've had a drink.
# Use your imagination.

g_game_items = {"notebook":
             {"description":
'''notebook containing all kinds of complex diagrams, equations, assignments
(many with very low grades), etc. in a completely random order. None of the
pages have any students names on them, but Mr. Schneider has obviously written
in the name "Peggy???" in red ink on several of the graded assignments.''',
              "takeable": True},
         "key":
             {"description": "small, nondescript key",
              "takeable": True}
}

# This is a handy utility routine that you give an action (like "take")
# and a command (like "take key"), and it returns just the item (e.g. "key")
def get_item_name(action, command):
    if command.startswith(action + " "):
        return command[len(action) + 1:]
    else:
        return None

# This is a handy utility routine that you give an item name (like "key")
# and it returns True if the user has that item, otherwise False.
def player_has_item(item_name):
    global g_player_items

    # Return true if the user has the item, otherwise false.
    return g_player_items.count(item_name) > 0

examine_item_command('computer lab', 'key')
