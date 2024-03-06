"""An interface for obtaining the temperature of GPU."""
from gpu_lib.managers.getter import TemperatureGetter


class NvidiaTemperatureGetter(TemperatureGetter):
    """An interface for obtaining the temperature of GPU."""

    async def get_temperature(self) -> float:
        """Obtain the temperature of GPU in Celsius.

        Returns:
            The temperature of GPU in Celsius.

        Raises:
            CommandError: If the exit code is not 0.
        """
        return float((await self._command_manager.execute_command(
            "/bin/nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader"))[0])
