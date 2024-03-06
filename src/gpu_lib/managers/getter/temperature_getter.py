"""An interface for obtaining the temperature of GPU."""
from abc import ABC, abstractmethod

from shell_executor_lib import CommandManager


class TemperatureGetter(ABC):
    """An interface for obtaining the temperature of GPU."""

    def __init__(self, command_manager: CommandManager):
        """Initialize the temperature getter.

        Args:
            command_manager: The command manager to use to execute commands.
        """
        self._command_manager = command_manager

    @abstractmethod
    async def get_temperature(self) -> float:
        """Obtain the temperature of GPU in Celsius.

        Returns:
            The temperature of GPU in Celsius.

        Raises:
            CommandError: If the exit code is not 0.
        """
        pass
