"""This error represents if the system can't detect a valid GPU driver."""


class DriverNotFound(Exception):
    """This error represents if the system can't detect a valid GPU driver."""

    def __init__(self) -> None:
        """Initialize the NotValidDriverError."""
        super().__init__("The system can't detect a valid GPU driver.")
