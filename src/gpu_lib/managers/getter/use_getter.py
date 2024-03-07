"""An interface for obtaining the use of GPU."""
from abc import ABC, abstractmethod

from shell_executor_lib import CommandManager


class UseGetter(ABC):
    """An interface for obtaining the use of GPU."""

    def __init__(self, command_manager: CommandManager):
        """Initialize the use getter.

        Args:
            command_manager: The command manager to use to execute commands.
        """
        self._command_manager = command_manager

    @abstractmethod
    async def get_use(self) -> float:
        """Obtain the use of GPU in percentage.

        Returns:
            The use of GPU.

        Raises:
            DriverNotFound: If the driver is not installed in the system.
            CommandError: If the exit code is not 0.
        """
        pass
