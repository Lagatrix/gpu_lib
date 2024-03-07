"""An interface for obtaining the information of GPU."""
from abc import ABC, abstractmethod

from shell_executor_lib import CommandManager


class InformationGetter(ABC):
    """An interface for obtaining the information of GPU."""

    def __init__(self, command_manager: CommandManager):
        """Initialize the information  getter.

        Args:
            command_manager: The command manager to use to execute commands.
        """
        self._command_manager = command_manager

    @abstractmethod
    async def get_gpu(self) -> tuple[str, str, str, str, str]:
        """Obtain the information of GPU.

        Returns:
            The information of GPU.

        Raises:
            DriverNotFound: If the driver is not installed in the system.
            CommandError: If the exit code is not 0.
        """
        pass
