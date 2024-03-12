"""Mocks of Nvidia GPU."""
from gpu_lib import Gpu
from gpu_lib.managers import NvidiaInformationGetter, NvidiaTemperatureGetter, NvidiaUseGetter

mock_temperature = ["50"]

mock_use_gpu = ["20 %"]

mock_information_gpu = [
    "Driver Version                            : 535.86.05",
    "Product Name                          : NVIDIA GeForce GTX 1050 Ti",
    "Product Brand                         : GeForce",
    "Product Architecture                  : Pascal",
    "    Total                             : 4096 MiB"
]

mock_information_gpu_tuple = ('NVIDIA GeForce GTX 1050 Ti', 'GeForce', 'Pascal', '4096 MiB', '535.86.05')

mock_nvidia_lspci_gpu = ["01:00.0 VGA compatible controller: NVIDIA Corporation GP107 [GeForce GTX 1050 Ti] (rev a1)"]

nvidia_getters_classes = (NvidiaInformationGetter, NvidiaTemperatureGetter, NvidiaUseGetter)

mock_nvidia_gpu_entity = Gpu(
    model="NVIDIA GeForce GTX 1050 Ti",
    brand="GeForce",
    architecture="Pascal",
    driver_version="535.86.05",
    memory="4096 MiB"
)
