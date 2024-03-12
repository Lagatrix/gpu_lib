"""Test the GpuManager class with Nvidia driver."""
import unittest
from unittest import mock

from shell_executor_lib import CommandManager

from gpu_lib import GpuManager
from tests.mock_gpu_lib import mock_information_gpu, mock_nvidia_gpu_entity, mock_temperature, mock_use_gpu
from tests.mock_gpu_lib import mock_command_executor_method, mock_nvidia_lspci_gpu


class TestNvidiaGpuManager(unittest.IsolatedAsyncioTestCase):
    """Test the GpuManager class with Nvidia driver."""

    def setUp(self) -> None:
        """Set up the test."""
        self.command_manager = CommandManager("augusto", "augusto")

    async def test_initiate_nvidia_gpu_manager(self) -> None:
        """Test initiate the GpuManager."""
        with mock.patch(mock_command_executor_method, return_value=mock_nvidia_lspci_gpu):
            self.assertIsInstance((await GpuManager.init(self.command_manager)), GpuManager)

    async def test_get_nvidia_gpu(self) -> None:
        """Test get the GPU information."""
        with mock.patch(mock_command_executor_method, side_effect=(mock_nvidia_lspci_gpu, mock_information_gpu)):
            gpu_manager = await GpuManager.init(self.command_manager)
            self.assertEqual(await gpu_manager.get_gpu(), mock_nvidia_gpu_entity)

    async def test_get_nvidia_gpu_temperature(self) -> None:
        """Test get the GPU temperature."""
        with mock.patch(mock_command_executor_method, side_effect=(mock_nvidia_lspci_gpu, mock_temperature)):
            gpu_manager = await GpuManager.init(self.command_manager)
            self.assertEqual(await gpu_manager.get_temperature(), 50)

    async def test_get_nvidia_gpu_use(self) -> None:
        """Test get the GPU use."""
        with mock.patch(mock_command_executor_method, side_effect=(mock_nvidia_lspci_gpu, mock_use_gpu)):
            gpu_manager = await GpuManager.init(self.command_manager)
            self.assertEqual(await gpu_manager.get_use(), 20)
