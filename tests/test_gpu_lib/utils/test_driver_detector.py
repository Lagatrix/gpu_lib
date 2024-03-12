"""Test the driver detector."""
import unittest
from unittest import mock

from shell_executor_lib import CommandManager

from gpu_lib import NotValidGpuError
from gpu_lib.utils import detect_driver
from tests.mock_gpu_lib import mock_command_executor_method, mock_nvidia_lspci_gpu, nvidia_getters_classes


class TestDriverDetector(unittest.IsolatedAsyncioTestCase):
    """Test the driver detector."""

    def setUp(self) -> None:
        """Set up the test."""
        self.command_manager = CommandManager("augusto", "augusto")

    async def test_get_nvidia_getters(self) -> None:
        """Test correctly get the nvidia getters."""
        with mock.patch(mock_command_executor_method, return_value=mock_nvidia_lspci_gpu):
            getter = await detect_driver(self.command_manager)
            for getter_class, getter_instance in zip(nvidia_getters_classes, getter):
                self.assertIsInstance(getter_instance, getter_class)

    async def test_not_valid_gpu(self) -> None:
        """Test not valid gpu."""
        with mock.patch(mock_command_executor_method, return_value=["unknown: unknown"]):
            with self.assertRaises(NotValidGpuError):
                await detect_driver(self.command_manager)
