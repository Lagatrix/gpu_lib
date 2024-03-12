"""Test the driver detector."""
import unittest
from unittest import mock

from shell_executor_lib import CommandManager

from gpu_lib import NotValidGpuError
from gpu_lib.managers import NvidiaTemperatureGetter, NvidiaUseGetter
from gpu_lib.managers.getter.nvidia.nvidia_information_getter import NvidiaInformationGetter
from gpu_lib.utils import detect_driver
from tests.mock_gpu_lib import mock_command_executor_method, mock_nvidia_lspci_gpu


class TestDriverDetector(unittest.IsolatedAsyncioTestCase):
    """Test the driver detector."""

    def setUp(self) -> None:
        """Set up the test."""
        self.command_manager = CommandManager("augusto", "augusto")

    async def test_get_nvidia_getters(self) -> None:
        """Test correctly get the nvidia getters."""
        with mock.patch(mock_command_executor_method, return_value=mock_nvidia_lspci_gpu):
            self.assertEqual(
                await detect_driver(self.command_manager),
                (NvidiaInformationGetter, NvidiaTemperatureGetter, NvidiaUseGetter)
            )

    async def test_not_valid_gpu(self) -> None:
        """Test not valid gpu."""
        with mock.patch(mock_command_executor_method, return_value=["unknown: unknown"]):
            with self.assertRaises(NotValidGpuError):
                await detect_driver(self.command_manager)
