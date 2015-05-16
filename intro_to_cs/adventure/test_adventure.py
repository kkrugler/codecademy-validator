import adventure_skeleton as adventure
import unittest
import string

class Adventure_Test(unittest.TestCase):

    def test_get_intro(self):
        intro_message = adventure.get_intro()
        total_chars = len(intro_message)

        self.assertGreater(total_chars, 0,
            "get_intro() didn't return any text.  \
Build and return a String containing the introduction message.")

        self.assertGreaterEqual(total_chars, 20,
            "get_intro() only returned a total of %d characters.  \
You can do better than that.  Get creative!" % total_chars)

    def test_get_goodbye(self):
        adventure.g_score = 42

        goodbye_message = adventure.get_goodbye()
        goodbye_lines = goodbye_message.splitlines()

        total_chars = 0
        is_found_score = False
        for line in goodbye_lines:
            total_chars += len(line)
            if (line.find("42") >= 0):
                is_found_score = True

        self.assertGreater(len(goodbye_lines), 0,
            "get_goodbye() didn't return any text.  \
Build and return a String containing the goodbye message.")

        self.assertGreaterEqual(total_chars, 20,
            "get_goodbye() only returned a total of %d characters.  \
You can do better than that.  Get creative!" % total_chars)

        self.assert_(is_found_score,
            "The goodbye message should include the user's score.")

    def test_get_help(self):
        help_message = adventure.get_help()
        help_lines = help_message.splitlines()

        num_printed_chars = 0
        command_descriptions = {
            'bye':None,
            'help':None,
            'list':None,
            'look':None,
            'check':None,
            'take':None,
            'drop':None,
            'examine':None
        }

        for line in help_lines:
            tokens = line.split()
            for token in tokens:
                token = token.strip(string.punctuation)
                if (command_descriptions.has_key(token)):
                    command_descriptions[token] = line

        for command in command_descriptions.keys():
            self.assertIsNotNone(command_descriptions.get(command),
                'get_help() did not describe the "%s" command' % command)
