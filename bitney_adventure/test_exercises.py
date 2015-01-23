import validator

g_exercise_names =  [   "print_intro",
                        "print_help",
                        "print_goodbye",
                        "print_room_description",
                        "print_items",
                        "check_move_command",
                        "check_general_command",
                        "move_to_room",
                        "take_item_command",
                        "examine_item_command",
                        "drop_item_command",
                        "check_item_command",
                        "game_complete"]

validator.test_exercises(g_exercise_names)
