class InvalidYear(Exception):
    def __init__(self, message):
        self.message = message


class InvalidFormat(Exception):
    def __init__(self, message):
        self.message = message
