from abc import ABC, abstractmethod
from typing import List
import numpy as np


class System(ABC):

    @property
    def state(self) -> np.ndarray:
        ...

    def transition(self, *args, **kwargs) -> None:
        ...




class Agent(System):
    def __init__(self, init_state: np.ndarray, cohesion: np.ndarray):
        self.alphabet = [0, 1]
        self.set_state(init_state)
        self.rows_number, self.columns_number = self.state.shape
        
        self.axis = (0 if self.rows_number > self.columns_number else 1)
        
        assert ((np.prod(init_state.shape) % 2) == 0) or (np.prod(init_state.shape) == 1), f'{self.state.shape=}'
        
        self.deepness = int(np.log2(np.prod(init_state.shape)))
        self.cohesion = cohesion
        assert self.cohesion.shape[0] == self.deepness

    @property
    def state(self) -> np.ndarray:
        return self.__state

    def set_state(self, state: np.ndarray) -> None:
        # TODO assert all([bit in self.alphabet for bit in state]), "state is not binary"
        self.__state = state
        
    def random_choice(self) -> np.ndarray:
        return np.random.choice(len(self.alphabet), self.state.shape)
        
    def transition(self, input_signal: np.ndarray) -> None:
        # print(self.state.shape)
        assert input_signal.shape == self.state.shape
        if self.deepness == 0:
            self.set_state(self.random_choice())
            return
        else:
            if self.axis == 1:
                a1 = self.state[: , : self.columns_number // 2]
                a2 = self.state[: , self.columns_number // 2 :]
            else: # axis = 0
                a1 = self.state[: self.rows_number // 2 , :]
                a2 = self.state[self.rows_number // 2 : , :]
            a1 = Agent(a1, self.cohesion[: -1])
            a2 = Agent(a2, self.cohesion[: -1])
            a1.transition(a2.state)
            a2.transition(a1.state)
            probable_state = np.concatenate([a1.state, a2.state], axis=self.axis)
            if (probable_state == input_signal).all():
                return
            else:
                self.set_state(probable_state)
        
    # information, entropy, cohesion (levels, ), self-organization, energy, accumulation, life, fraktals
    # TODO

    # def foo(self):
    #     for level in range(self.deepness):
    #         axis = int(((-1)**level + 1) / 2)
    #         vector_w = int(2**((level-(1-axis))/2))
    #         if axis == 1:
    #             vector_n = int((self.columns_number // vector_w) // 2)
    #             a_1 = np.concatenate([self.state[: , 2*vector_i*vector_w : (2*vector_i+1)*vector_w] for vector_i in range(vector_n)], axis=axis)
    #             a_2 = np.concatenate([self.state[: , (2*vector_i-1)*vector_w : (2*vector_i-1+1)*vector_w] for vector_i in range(1, vector_n+1)], axis=axis)
    #         else:
    #             vector_n = int((self.rows_number // vector_w) // 2)
    #             a_1 = np.concatenate([self.state[2*vector_i*vector_w : (2*vector_i+1)*vector_w , :] for vector_i in range(vector_n)], axis=axis)
    #             a_2 = np.concatenate([self.state[(2*vector_i-1)*vector_w : (2*vector_i-1+1)*vector_w , :] for vector_i in range(1, vector_n+1)], axis=axis)
    #         print((level, axis, vector_w, vector_n))
    #         print()
    #         print(a_1)
    #         print()
    #         print(a_2)
    #         print()
    #         print()


# class Group(System):
#     def __init__(self, agents: List[Agent]):
#         ...

#     @property
#     def state(self) -> np.ndarray:
#         ...
        
#     def transition(self, *args, **kwargs) -> None:
#         ...
    
            
        
