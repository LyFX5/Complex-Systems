from abc import ABC, abstractmethod
from typing import List
from copy import copy
import numpy as np


class System(ABC):

    @property
    def state(self) -> np.ndarray:
        ...

    def transition(self, *args, **kwargs) -> None:
        ...


class MultiAgent(System):
    def __init__(self, init_state: np.ndarray, spherical: bool):
        self.alphabet = [0, 1]
        self.set_state(init_state)
        self.spherical = spherical
        
    @property
    def state(self) -> np.ndarray:
        return self.__state

    @property
    def information(self) -> float:
        # TODO
        return ...

    @property
    def entropy(self) -> float:
        # TODO
        return ...

    def set_state(self, state: np.ndarray) -> None:
        self.__state = copy(state)
        
    def random_choice(self) -> np.ndarray:
        return np.random.choice(len(self.alphabet), self.state.shape)

    def transition(self) -> None:
        # next_state = copy(self.state)
        # self.set_state(next_state)  
        self.transition_life_game()

    def map_life_game(self, current, neighbors: List) -> float:
        if (sum(neighbors) < 2) or (sum(neighbors) > 3):
            return 0
        else:
            if current == 0:
                if sum(neighbors) == 3:
                    return 1
            return current
            
    def transition_life_game(self) -> None:
        next_state = copy(self.state)
        n, m = self.state.shape
        if not self.spherical:
            for i in range(1, n-1):
                for j in range(1, m-1):
                    r = self.state[i][j+1]
                    rt = self.state[i-1][j+1]
                    t = self.state[i-1][j]
                    lt = self.state[i-1][j-1]
                    l = self.state[i][j-1]
                    lb = self.state[i+1][j-1]
                    b = self.state[i+1][j]
                    rb = self.state[i+1][j+1]
                    current = self.state[i][j]
                    neighbors = [r, rt, t, lt, l, lb, b, rb]
                    next_state[i][j] = self.map_life_game(current, neighbors)
        else:
            for i in range(n):
                for j in range(m):
                    r = self.state[i][(j+1) % m]
                    rt = self.state[(i-1) % n][(j+1) % m]
                    t = self.state[(i-1) % n][j]
                    lt = self.state[(i-1) % n][(j-1) % m]
                    l = self.state[i][(j-1) % m]
                    lb = self.state[(i+1) % n][(j-1) % m]
                    b = self.state[(i+1) % n][j]
                    rb = self.state[(i+1) % n][(j+1) % m]
                    current = self.state[i][j]
                    neighbors = [r, rt, t, lt, l, lb, b, rb]
                    next_state[i][j] = self.map_life_game(current, neighbors)
        self.set_state(next_state)   
        
    
        
