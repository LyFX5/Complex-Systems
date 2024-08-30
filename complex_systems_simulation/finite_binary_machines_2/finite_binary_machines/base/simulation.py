from typing import Iterator
import numpy as np
from .system import System


class Simulation(Iterator):
    def __init__(self, group: System, steps_number: int):
        self.group = group
        self.steps_number = steps_number
        
    def __next__(self) -> np.ndarray:
        self.group.transition()
        return self.group.state

    def __iter__(self) -> Iterator:
        return self
        