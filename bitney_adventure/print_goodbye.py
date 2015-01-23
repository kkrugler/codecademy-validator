def print_goodbye():
    global g_score

    # Print goodbye text, along with the player's current score

    print '''We're sad to see you go, so hurry back.
Your total score was %d, by the way.''' % g_score

#####################################################
# WARNING! DO NOT MODIFY THE CODE BELOW THIS POINT! #
#####################################################

# This is the player's current score. They get points for visiting a room
# (but only the first time!)
#
g_score = 42

print_goodbye()
