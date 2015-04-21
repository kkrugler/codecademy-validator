# The following function definition returns a "cleaned up"
# version of the name passed by the caller, capitalizing the
# first letter of the first and last names (and making sure the
# rest of the letters are lowercase).
# DO NOT modify the code in this function definition.
def normalize_name(name):
    name = name.lower()
    name = name[0].upper() + name[1:]
    pos = name.find(' ') + 1
    if (pos > 0):
        name = name[:pos] + name[pos].upper() + name[pos+1:]
    return name

# Here we use normalize_name() to clean up three example names,
# sending the results from the first two invocations to the
# console.
# DO NOT modify the code in this section.
print normalize_name('cHRIs')
print normalize_name('cHRIs SchneideR')
name = 'KEN krugler'
normalized_name = normalize_name(name)

# Predict the value of each of the two variables above at this
# point in the program by assigning the two variables below to
# String literals:
name_prediction = 'KEN krugler'
normalized_name_prediction = 'Ken Krugler'

# The following function definition doubles the score passed to
# it, but never returns a score larger than 100.
# DO NOT modify the code in this function definition.
def double_score(score):
    score = score * 2
    if (score > 100):
        score = 100
    return score

# Here we use double_score() to double a few example scores,
# again sending the results from the first two invocations to the
# console.
# DO NOT modify the code in this section.
print double_score(12)
print double_score(55)
score = 35
doubled_score = double_score(score)

# Predict the value of each of the two variables above at this
# point in the program by assigning the two variables below to
# String literals:
score_prediction = 35
doubled_score_prediction = 70

# The following function definition uses the other two functions
# to both clean up the player name and double the player's score.
# DO NOT modify the code in this function definition.
def double_player_score(player_info):
    old_player_info = [player_info[0], player_info[1]]
    player_info[0] = normalize_name(player_info[0])
    player_info[1] = double_score(player_info[1])
    return old_player_info

# Here we use double_player_score() on some example player
# information.
# DO NOT modify the code in this section.
player_info_1 = [name, doubled_score]
player_info_2 = double_player_score(player_info_1)

# Predict the value of each of the two variables above at this
# point in the program by assigning the two variables below to
# String literals containing their string representations:
player_info_1_prediction = "['Ken Krugler', 100]"
player_info_2_prediction = "['KEN krugler', 70]"
