class InvalidEnvironmentVariable(Exception):
    def __init__(self, message):
        self.message = message


class RestApiException(Exception):
    def __init__(self, message):
        self.message = message
