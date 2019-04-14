
class BookNotFoundException(Exception):
    """Raised when aa book is not found

    Attributes:
       Message - Reason for book not found
    """

    def __init__(self, message):
        self.message = message

class InvalidBookException(Exception):
    """Raised when aa book is not found

    Attributes:
       Message - Reason for book not found
    """
    def __init__(self, message):
        self.message = message