"""Test the information nvidia getter."""
import unittest
from unittest import mock

from shell_executor_lib import CommandManager, CommandError

from gpu_lib import DriverNotFound
from gpu_lib.managers.getter.nvidia.nvidia_information_getter import NvidiaInformationGetter
from tests.mock_gpu_lib import mock_command_executor_method, mock_information_gpu, mock_information_gpu_tuple


class TestNvidiaInformationGetter(unittest.IsolatedAsyncioTestCase):
    """Test the information nvidia getter."""

    def setUp(self) -> None:
        """Set up the test."""
        self.information_getter = NvidiaInformationGetter(CommandManager("augusto", "augusto"))

    async def test_get_gpu_information(self) -> None:
        """Test correctly get the information of GPU."""
        with mock.patch(mock_command_executor_method, return_value=mock_information_gpu):
            self.assertEqual(await self.information_getter.get_gpu(), mock_information_gpu_tuple)

    async def test_get_gpu_information_without_driver(self) -> None:
        """Test get the information of GPU when the driver is not found."""
        with mock.patch(mock_command_executor_method, side_effect=CommandError(127, "No driver")):
            with self.assertRaises(DriverNotFound):
                await self.information_getter.get_gpu()

    async def test_get_gpu_information_unknown_error(self) -> None:
        """Test get the information of GPU when an unknown error occurs."""
        with mock.patch(mock_command_executor_method, side_effect=CommandError(1, "Error")):
            with self.assertRaises(CommandError):
                await self.information_getter.get_gpu()
