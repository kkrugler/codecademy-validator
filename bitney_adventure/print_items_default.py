def print_items():
    # Level - 5

    global g_player_items

    # TODO print a list of the item names that the player has, which
    # means a loop that iterates over the g_game_items list, and prints
    # out the list. If the player has nothing, print "You've got nothing"

    print "You've got nothing"

# This is a list of names of items that player has taken. It starts off
# as empty. When you take an item, it gets added to this list, and when
# you drop an item, it gets removed from this list.
g_player_items = ["notebook", "key"]


print_items()
