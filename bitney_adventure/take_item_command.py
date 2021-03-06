def take_item_command(room_name, command):
    global g_rooms
    global g_player_items

    # First use the handy-dandy get_item_name utility function
    # to extract the item name from the command.
    item_name = get_item_name("take", command)

    # If it's just "take" then return an appropriate
    # error message.
    if (not item_name):
        print "You didn't specify what to take"
        return

    # Get the current room by name
    room = g_rooms[room_name]

    # Get the room's item list
    room_item_names = room['items']

    # If xxx isn't the name of an item in the room, then
    # return a different error message.
    if (room_item_names.count(item_name) == 0):
        print "There is no %s in this room" % item_name
        return

    # Otherwise, move the item from the room's list of items,
    # add the item to the player's inventory,
    # and print a confirmation string
    room_item_names.remove(item_name)
    g_player_items.append(item_name)
    print "You now have the %s" % item_name

# This is a list of names of items that player has taken. It starts off
# as empty. When you take an item, it gets added to this list, and when
# you drop an item, it gets removed from this list.
g_player_items = ["key"]

# rooms is a dictionary, where the key is the room name, and the value is a "room"
# Each room is also a dictionary, where the key is one of several possible values
#   description -> string that describes the room. This should include all doors.
#   items -> list of item names for items found in that room
#   value -> points for visiting the room
#   doors -> dictionary that maps from a door name ("north", "up", etc) to a room name
#
# You can also have other room-specific attributed, e.g. the computer lab could have
# a "locked": True attribute, and you have to unlock it first before you can go through
# that door. Use your imagination.

g_rooms = {"computer lab":
             {"description": "The computer lab is filled with glowing screens and old chairs. There is a door to the south",
              "items": ["notebook"],
              "value": 5,
              "doors": {"south": "hallway"}},
         "hallway":
             {"description": "The hallway is filled with colorful murals. There are doors to the north and east",
              "items": ["key"],
              "value": 0,
              "doors": {"north": "computer lab", "east": "lobby"}},
         "lobby":
             {"description": "The lobby is a place where people go to chill. There is a door to the west",
              "items": [],
              "value": 2,
              "doors": {"west": "hallway"}},
}

# This is a handy utility routine that you give an action (like "take")
# and a command (like "take key"), and it returns just the item (e.g. "key")
def get_item_name(action, command):
    if command.startswith(action + " "):
        return command[len(action) + 1:]
    else:
        return None

take_item_command("computer lab", "notebook")
