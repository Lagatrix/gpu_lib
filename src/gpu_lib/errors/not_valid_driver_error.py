"""This error represents if the system can't detect a valid GPU driver."""


class NotValidDriverError(Exception):
    """This error represents if the system can't detect a valid GPU driver."""

    def __init__(self) -> None:
        """Initialize the NotValidDriverError."""
        super().__init__("The system can't detecto a valid driver.")
