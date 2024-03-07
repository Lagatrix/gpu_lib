"""Obtain the information of GPU."""
from shell_executor_lib import CommandError

from gpu_lib import DriverNotFound
from gpu_lib.managers.getter import InformationGetter


class NvidiaInformationGetter(InformationGetter):
    """Obtain the information of GPU."""

    async def get_gpu(self) -> tuple[str, str, str, str, str]:
        """Obtain the information of GPU.

        Returns:
            The information of GPU.

        Raises:
            DriverNotFound: If the driver is not installed in the system.
            CommandError: If the exit code is not 0.
        """
        try:
            command_filter: str = '/Product Name|Product Brand|Product Architecture|Driver Version|Total/'
            data_list: list[str] = await (self._command_manager.execute_command
                                          (f"/bin/nvidia-smi -a | /bin/awk '{command_filter}'"))

            return (data_list[1].split(": ")[1], data_list[2].split(": ")[1], data_list[3].split(": ")[1],
                    data_list[4].split(": ")[1], data_list[0].split(": ")[1])

        except CommandError as command_error:
            if command_error.status_code == 127:
                raise DriverNotFound()
            raise command_error
