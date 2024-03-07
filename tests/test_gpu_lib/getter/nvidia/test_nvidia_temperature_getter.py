"""Test the temperature nvidia getter."""
import unittest
from unittest import mock

from shell_executor_lib import CommandManager, CommandError

from gpu_lib import DriverNotFound
from gpu_lib.managers.getter import NvidiaTemperatureGetter
from tests.mock_gpu_lib import mock_command_executor_method, mock_temperature


class TestNvidiaTemperatureGetter(unittest.IsolatedAsyncioTestCase):
    """Test the temperature nvidia getter."""

    def setUp(self) -> None:
        """Set up the test."""
        self.temperature_getter = NvidiaTemperatureGetter(CommandManager("augusto", "augusto"))

    async def test_get_gpu_temperature(self) -> None:
        """Test correctly get the information of GPU."""
        with mock.patch(mock_command_executor_method, return_value=mock_temperature):
            self.assertEqual(await self.temperature_getter.get_temperature(), 50)

    async def test_get_gpu_temperature_without_driver(self) -> None:
        """Test get the information of GPU when the driver is not found."""
        with mock.patch(mock_command_executor_method, side_effect=CommandError(127, "No driver")):
            with self.assertRaises(DriverNotFound):
                await self.temperature_getter.get_temperature()

    async def test_get_gpu_temperature_unknown_error(self) -> None:
        """Test get the information of GPU when an unknown error occurs."""
        with mock.patch(mock_command_executor_method, side_effect=CommandError(1, "Error")):
            with self.assertRaises(CommandError):
                await self.temperature_getter.get_temperature()
