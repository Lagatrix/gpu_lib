"""Obtain information of the GPU."""
from shell_executor_lib import CommandManager

from gpu_lib import Gpu
from gpu_lib.managers import InformationGetter, TemperatureGetter, UseGetter
from gpu_lib.utils import detect_driver


class GpuManager:
    """Obtain information of the GPU."""

    @classmethod
    async def init(cls, command_manager: CommandManager) -> 'GpuManager':
        """Initialize the gpu manager getter.

        Args:
            command_manager: The command manager to use to execute commands.

        Raises:
            NotValidGpuError: If the GPU is not supported.
            CommandError: If the error is not expected.
        """
        return cls(await detect_driver(command_manager))

    def __init__(self, getters: tuple[InformationGetter, TemperatureGetter, UseGetter]):
        """Initialize the gpu manager getter.

        Args:
            getters: A tuple with the getters to obtain the information of GPU.
        """
        self.__information_getter = getters[0]
        self.__temperature_getter = getters[1]
        self.__use_getter = getters[2]

    async def get_gpu(self) -> Gpu:
        """Get the GPU information.

        Returns:
            The GPU information.

        Raises:
            DriverNotFound: If the driver is not installed in the system.
            CommandError: If the error is not expected.
        """
        information = await self.__information_getter.get_gpu()

        return Gpu(
            model=information[0],
            brand=information[1],
            architecture=information[2],
            driver_version=information[4],
            memory=information[3]
        )

    async def get_temperature(self) -> float:
        """Get the GPU temperature.

        Returns:
            The GPU temperature.

        Raises:
            DriverNotFound: If the driver is not installed in the system.
            CommandError: If the error is not expected.
        """
        return await self.__temperature_getter.get_temperature()

    async def get_use(self) -> float:
        """Get the GPU use.

        Returns:
            The GPU use.

        Raises:
            DriverNotFound: If the driver is not installed in the system.
            CommandError: If the error is not expected.
        """
        return await self.__use_getter.get_use()
