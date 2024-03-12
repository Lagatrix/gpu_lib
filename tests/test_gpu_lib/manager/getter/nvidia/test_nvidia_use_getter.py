"""Test the use nvidia getter."""
import unittest
from unittest import mock

from shell_executor_lib import CommandManager, CommandError

from gpu_lib import DriverNotFound
from gpu_lib.managers.getter.nvidia.nvidia_use_getter import NvidiaUseGetter
from tests.mock_gpu_lib import mock_use_gpu
from tests.mock_gpu_lib import mock_command_executor_method


class TestNvidiaUseGetter(unittest.IsolatedAsyncioTestCase):
    """Test the use nvidia getter."""

    def setUp(self) -> None:
        """Set up the test."""
        self.use_getter = NvidiaUseGetter(CommandManager("augusto", "augusto"))

    async def test_get_gpu_use(self) -> None:
        """Test correctly get the information of GPU."""
        with mock.patch(mock_command_executor_method, return_value=mock_use_gpu):
            self.assertEqual(await self.use_getter.get_use(), 20)

    async def test_get_gpu_use_without_driver(self) -> None:
        """Test get the information of GPU when the driver is not found."""
        with mock.patch(mock_command_executor_method, side_effect=CommandError(127, "No driver")):
            with self.assertRaises(DriverNotFound):
                await self.use_getter.get_use()

    async def test_get_gpu_use_unknown_error(self) -> None:
        """Test get the information of GPU when an unknown error occurs."""
        with mock.patch(mock_command_executor_method, side_effect=CommandError(1, "Error")):
            with self.assertRaises(CommandError):
                await self.use_getter.get_use()
