"""This utils detect the driver of GPU."""
from typing import cast

from shell_executor_lib import CommandManager

from gpu_lib import NotValidGpuError
from gpu_lib.managers import NvidiaInformationGetter, NvidiaUseGetter, NvidiaTemperatureGetter
from gpu_lib.managers import InformationGetter, TemperatureGetter, UseGetter

drivers_map = {
    "nvidia": (NvidiaInformationGetter, NvidiaTemperatureGetter, NvidiaUseGetter),
}


async def detect_driver(command_manager: CommandManager) -> tuple[InformationGetter, TemperatureGetter, UseGetter]:
    """Detect the driver of GPU.

    Args:
        command_manager: The command manager to execute commands.

    Returns:
        The getters to obtain the information of GPU in this order: InformationGetter, TemperatureGetter, UseGetter.

    Raises:
        NotValidGpuError: If the GPU is not supported.
        CommandError: If the error is not expected.
    """
    vga: str = (await command_manager.execute_command("/bin/lspci | grep VGA"))[0].split(": ")[1].lower()

    for driver, getters in drivers_map.items():
        if driver in vga:
            return cast(
                tuple[InformationGetter, TemperatureGetter, UseGetter],
                tuple(getter(command_manager) for getter in getters)
            )

    raise NotValidGpuError(vga)
