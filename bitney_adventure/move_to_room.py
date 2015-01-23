def move_to_room(room_name):
    global g_current_room_name
    global g_visited_room_names
    global g_score

    # Update the global current room name.
    g_current_room_name = room_name

    # If this is the first time in this room (check visited_rooms) then
    # add the room's score to the player's score, and print a msg
    # about how many points they've earned.
    if (g_visited_room_names.count(room_name) > 0):
        print "You are in the %s" % room_name

    # Remember that the user has now been here
    g_visited_room_names.append(room_name)

    # Print the room description
    print_room_description(room_name)

    # Get the new room by name
    room = g_rooms[room_name]

    # The player has earned the new room's value
    room_value = room['value']
    g_score += room_value

    # Congratulate the player on his/her progress
    if (room_value > 0):
        print "You just earned %s points!" % room_value

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

move_to_room('computer lab')
