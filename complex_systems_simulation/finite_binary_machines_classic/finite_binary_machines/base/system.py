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
    def __init__(self, init_state: np.ndarray):
        self.alphabet = [0, 1]
        self.set_state(init_state)
        self.life_rule_dict = {'0000': 0,
                         '0001': 1,
                         '0010': 1,
                         '0011': 1,
                         '0100': 0,
                         '0101': 1,
                         '0110': 1,
                         '0111': 0,
                         '1000': 0,
                         '1001': 0,
                         '1010': 0,
                         '1011': 0,
                         '1100': 0,
                         '1101': 0,
                         '1110': 0,
                         '1111': 0} 
        # self.rule_dict = {'000': 0,
        #                   '001': 1,
        #                   '010': 1,
        #                   '011': 1,
        #                   '100': 0,
        #                   '101': 1,
        #                   '110': 1,
        #                   '111': 0} 
        self.rule_dict = {'000': 0,
                          '001': 1,
                          '010': 1,
                          '011': 1,
                          '100': 1,
                          '101': 0,
                          '110': 0,
                          '111': 0} 
        
    @property
    def state(self) -> np.ndarray:
        return self.__state

    def set_state(self, state: np.ndarray) -> None:
        # TODO assert all([bit in self.alphabet for bit in state]), "state is not binary"
        self.__state = state
        
    def random_choice(self) -> np.ndarray:
        return np.random.choice(len(self.alphabet), self.state.shape)

    # def map(self, neighbors: List) -> float:
    #     assert len(neighbors) == 4, f'{neighbors=}'
    #     neighbors_string = ''
    #     for neighbor in neighbors: neighbors_string += str(int(neighbor))
    #     bit_new_state = self.rule_dict[neighbors_string]
    #     return bit_new_state

    def map_life_game(self, current, neighbors: List) -> float:
        # triple_string = str(int(neighbors[2])) + str(int(current)) + str(int(neighbors[0]))
        # return self.rule_dict[triple_string]
        if (sum(neighbors) < 2) or (sum(neighbors) > 3):
            return 0
        else:
            if current == 0:
                if sum(neighbors) == 3:
                    return 1
            return current
            
    def transition(self) -> None:
        next_state = copy(self.state)
        n, m = self.state.shape
        for i in range(n):
            for j in range(m):
                r = self.state[i][(j+1) % m]
                t = self.state[(i+1) % n][j]
                l = self.state[i][(j-1) % m]
                b = self.state[(i-1) % n][j]
                next_state[i][j] = self.map_life_game(self.state[i][j], [r, t, l, b])
        self.set_state(next_state)   
        
    
        