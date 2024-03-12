"""Obtain the use of GPU."""
from shell_executor_lib import CommandError

from gpu_lib import DriverNotFound
from gpu_lib.managers.getter import UseGetter


class NvidiaUseGetter(UseGetter):
    """Obtain the use of GPU."""

    async def get_use(self) -> float:
        """Obtain the use of GPU in percentage.

        Returns:
            The use of GPU.

        Raises:
            DriverNotFound: If the driver is not installed in the system.
            CommandError: If the exit code is not 0.
        """
        try:
            return float((await self._command_manager.execute_command(
                "/bin/nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader"))[0].split(" ")[0])
        except CommandError as command_error:
            if command_error.status_code == 127:
                raise DriverNotFound()
            raise command_error
