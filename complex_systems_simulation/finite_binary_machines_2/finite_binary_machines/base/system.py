import numpy as np


class System:
    def __init__(self, init_state: np.ndarray):
        self.alphabet = [0, 1]
        self.set_state(init_state)

    @property
    def state(self) -> np.ndarray:
        return self.__state

    def set_state(self, state: np.ndarray) -> None:
        # TODO assert all([bit in self.alphabet for bit in state]), "state is not binary"
        self.__state = state
        
    def random_choice(self) -> np.ndarray:
        return np.random.choice(len(self.alphabet), self.state.shape)
        
    def transition(self, *args, **kwargs) -> None:
        self.set_state(self.random_choice())

    # information, entropy, cohesion (levels, ), self-organization, energy, accumulation, life, fraktals
    # TODO
