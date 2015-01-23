def check_general_command(room_name, command):
    # Level - 2

    # TODO see if the command is one that we want to respond to, without
    # doing anything. E.g. if they're swearing at us, tell them to keep
    # it clean. If we don't have any match, return False.

    if command.startswith("hit"):
        print "There's no violence allowed at Bitney!"
        return True
    else:
        return False

check_general_command("complement", "Mr. Schneider")
