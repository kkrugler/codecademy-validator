def check_move_command(room_name, command):
    # Level - 4

    global g_rooms

    # TODO see if this is the name of a door in this room.
    # If so, call move_to_room() and return True.  Otherwise return False.

    return False

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

def move_to_room(room_name):
    # Level - 5

    global g_current_room_name
    global g_visited_room_names
    global g_score

    # TODO set the current_room to be room.
    # If this is the first time in this room (check visited_rooms) then
    # add the room's score to the player's score, and let them know they
    # just earned some additional points. Also print out the room's
    # description if it's the first time, otherwise just the room name.

check_move_command("hallway", "north")
