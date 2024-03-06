"""Test the temperature nvidia getter."""
import unittest
from unittest import mock

from shell_executor_lib import CommandManager

from gpu_lib.managers.getter import NvidiaTemperatureGetter
from tests.mock_gpu_lib import mock_command_executor_method, mock_temperature


class TestNvidiaTemperatureGetter(unittest.IsolatedAsyncioTestCase):
    """Test the temperature nvidia getter."""

    def setUp(self) -> None:
        """Set up the test."""
        self.temperature_getter = NvidiaTemperatureGetter(CommandManager("augusto", "augusto"))

    async def test_get_cpu_info(self) -> None:
        """Test correctly get the information of CPU."""
        with mock.patch(mock_command_executor_method, return_value=mock_temperature):
            self.assertEqual(await self.temperature_getter.get_temperature(), 50)
