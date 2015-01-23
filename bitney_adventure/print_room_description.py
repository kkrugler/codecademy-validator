def print_room_description(room_name):
    global g_rooms

    # Retrieve the current room by name
    room = g_rooms[room_name]

    # Print the room's description
    print room['description']

    # Get the room's item list
    item_names = room['items']

    # Print a comma-separated list of the room's items, if any.
    if (item_names):
        items_text = "the room contains the following items: "
        for item_name in item_names:
            items_text += (item_name + ", ")
        items_text = items_text[:-2] # remove that last comma & space
        print items_text

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

print_room_description("hallway")
