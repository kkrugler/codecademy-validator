def print_room_description(room_name):
    # Level - 5

    global g_rooms

    # TODO print the room's description and list the items it currently
    # contains, which means a loop that iterates over its item list,
    # (which you retrieve from the "items" entry in the g_rooms
    # dictionary), and then prints out the list. If the list contains
    # no items, skip that part.

    print "room description"

#####################################################
# WARNING! DO NOT MODIFY THE CODE BELOW THIS POINT! #
#####################################################

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

g_rooms = {"Computer Lab":
             {"description": "The computer lab is filled with glowing screens and old chairs. There is a door to the south",
              "items": ["notebook"],
              "value": 5,
              "doors": {"south": "Hallway"}},
         "Hallway":
             {"description": "The hallway is filled with colorful murals. There are doors to the north and east",
              "items": ["key", "donut", "hamster"],
              "value": 0,
              "doors": {"north": "Computer Lab", "east": "Lobby"}},
         "Lobby":
             {"description": "The lobby is a place where people go to chill. There is a door to the west",
              "items": [],
              "value": 2,
              "doors": {"west": "Hallway"}},
}

print_room_description("Hallway")
