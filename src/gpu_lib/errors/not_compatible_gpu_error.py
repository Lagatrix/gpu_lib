"""TThis error represents if the system contains not compatible GPU."""


class NotValidGpuError(Exception):
    """This error represents if the system contains not compatible GPU."""

    def __init__(self, gpu: str) -> None:
        """Initialize the NotValidGpuError.

        Args:
            gpu: The name of invalid GPU.
        """
        super().__init__(f"The gpu: {gpu} is not supported.")
