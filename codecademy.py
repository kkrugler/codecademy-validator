import sys

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.messages = []

    def write(self, message):
        self.terminal.write(message)
        self.messages.append(message)

    def getMessages(self):
        return self.messages


class Codecademy:
    def __init__(self):
        self.globals = {}
        self.code = ""
        self.messages = []
        self.result = None
        self.error = None

    def eval(self, filename):
        logger = Logger()
        sys.stdout = logger

        self.code = open(filename).read();
        try:
            execfile(filename, self.globals)
        except Exception as e:
            self.error = e

        for message in logger.getMessages():
            if (message != "\n"):
                self.messages.append(message)

        sys.stdout = logger.terminal

    def setResult(self, result):
        self.result = result

    def printed(self, message):
        for msg in self.messages:
            if message == msg:
                return True

        return False

    def prints(self):
        return self.messages

SINGLETON = Codecademy()
