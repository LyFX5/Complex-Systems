import numpy as np
from typing import List
from .system import System


class FiniteBinaryMachine(System):
    def __init__(self, init_state: np.ndarray):
        self.alphabet = [0, 1]
        self.set_state(init_state)
        self.dimension = self.__state.shape[0] 
        # number of variables / parameters / negentropy (if effective only) / number of bits / information

    @property
    def state(self) -> np.ndarray:
        return self.__state

    def set_state(self, state: np.ndarray) -> None:
        assert all([bit in self.alphabet for bit in state]), "state is not binary"
        self.__state = state

    def random_chice(self) -> np.ndarray:
        return np.random.choice(self.alphabet, self.dimension).reshape((self.dimension, 1))

    def transition(self, *args, **kwargs) -> None:
        self.set_state(self.random_chice())


class CommunicationAgent(FiniteBinaryMachine):
    def __init__(self, init_state: np.ndarray):
        super(CommunicationAgent, self).__init__(init_state=init_state)
        self.channels: List[FiniteBinaryMachine] = []

    def transition(self) -> None:
        probable_state = self.random_chice()
        for channel in self.channels:
            if (probable_state == channel.state).all():
                return
        self.set_state(probable_state)

    def set_channels(self, channels: List[FiniteBinaryMachine]):
        self.channels = channels
        