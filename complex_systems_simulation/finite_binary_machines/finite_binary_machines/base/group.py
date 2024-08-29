import numpy as np
from typing import List
from copy import copy
from .system import System
from .agent import CommunicationAgent


class MultiAgentSystem(System):
    def __init__(self, agents: [System]):
        self.agents = agents

    @property
    def state(self) -> np.ndarray:
        return np.concatenate([agent.state for agent in self.agents], axis=1)

    def transition(self, *args, **kwargs) -> None:
        for agent in self.agents:
            agent.transition()


class CommunicationGroup(MultiAgentSystem):
    def __init__(self, agents: [CommunicationAgent]):
        super(CommunicationGroup, self).__init__(agents=agents)
        self.agents_number = len(agents)
        self.adjacency_matrix = np.zeros((self.agents_number, self.agents_number))

    def set_adjacency_matrix(self, adjacency_matrix: np.ndarray):
        self.adjacency_matrix = copy(adjacency_matrix)

    def build_net(self):        
        for j in range(len(self.agents)):
            self.adjacency_matrix[j][j] = 0
            channels = []
            for c in range(len(self.agents)):
                if self.adjacency_matrix[j][c] == 1:
                    channels.append(self.agents[c])
            self.agents[j].set_channels(channels)
        