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

# This is the name of the current room that the player is in.
g_current_room_name = "computer lab"

# This is a list of all of names of all the rooms that the player has visited.
# It starts off with just the current room that they're in.
g_visited_room_names = ["hallway"]

# This is the player's current score. They get points for visiting a room
# (but only the first time!)
g_score = 0

def print_room_description(room_name):
    print "This is a fake description of the lovely %s!" % room_name

move_to_room("computer lab")
