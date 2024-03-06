"""This entity represents a GPU."""
from dataclasses import dataclass


@dataclass
class Gpu:
    """This entity represents a GPU.

    Args:
        model: The model of the GPU.
        brand: The brand of the GPU.
        architecture: The architecture of the GPU.
        speed: The speed of the GPU.
        memory: The memory of the GPU.
        driver_version: The driver version of the GPU.
    """
    model: str
    brand: str
    architecture: str
    speed: int
    memory: str
    driver_version: str
