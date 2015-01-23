def game_complete():
    # Level - 3

    global g_visited_room_names
    global g_score

    # TODO decide when to congratulate user and return True. This would
    # be the case for when they've visited every room. So you can either
    # compare their score against the sum of scores from every room, or
    # if the g_visited_room_names list length is == the number of rooms.

    return False

# This is a list of all of names of all the rooms that the player has visited.
# It starts off with just the current room that they're in.
g_visited_room_names = ['hallway', 'computer lab']

# This is the player's current score. They get points for visiting a room
# (but only the first time!)
g_score = 10

game_complete()
