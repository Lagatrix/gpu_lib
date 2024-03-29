"""Obtain the temperature of GPU."""
from shell_executor_lib import CommandError

from gpu_lib.errors import DriverNotFound
from gpu_lib.managers.getter import TemperatureGetter


class NvidiaTemperatureGetter(TemperatureGetter):
    """Obtain the temperature of GPU."""

    async def get_temperature(self) -> float:
        """Obtain the temperature of GPU in Celsius.

        Returns:
            The temperature of GPU in Celsius.

        Raises:
            DriverNotFound: If the driver is not installed in the system.
            CommandError: If the exit code is not 0.
        """
        try:
            return float((await self._command_manager.execute_command(
                "/bin/nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader"))[0])
        except CommandError as command_error:
            if command_error.status_code == 127:
                raise DriverNotFound()
            raise command_error
