

class ExceptionBase(ValueError):
    def __init__(self, messages):
        if not isinstance(messages, list):
            messages = [messages]
        super().__init__(messages)

