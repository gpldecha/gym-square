# -*- coding: utf-8 -*-
"""
@author: Guillaume de Chambrier

    A simple square world.
    State: Continuous
    Action: Discrete
"""

import math
import gym
from gym import spaces
from gym.utils import seeding
import numpy as np

from square_world.square_world import SquareWorld
from square_world.reward import Reward


class SquareContinuousStateEnv(gym.Env):

    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 30
    }

    def __init__(self):
        self._seed()
        self.reset()

        self.square_world       = SquareWorld(state='continuous')
        self.action_space       = spaces.Discrete(4)
        self.observation_space  = self.square_world.get_observation_space()

        # control command to agent
        self._u = np.array([0,0],dtype=float)

    def set_reward(self,reward):
        self.square_world.reward = reward

    def sample_observations(self,m):
        """ Returns a set of m randomely sampled observations from the observations
            space.
            Args:
                m   : init      , number of samples
            Returns:
                np.array((m,2)) , a 2-dimensional array of m states
        """
        obs_space = self.square_world.get_observation_space()
        min_val   = obs_space[0]
        max_val   = obs_space[1]
        return np.random.uniform(min_val,max_val,(m,2))


    def _seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def _step(self, action):
        assert self.action_space.contains(action), "%r (%s) invalid" % (action, type(action))
        if action == 0:
            # right
            self._u[0]      =  0.05
            self._u[1]      =  0
        elif action == 1:
            # left
            self._u[0]      = -0.05
            self._u[1]      =  0
        elif action == 2:
            # up
            self._u[0]      =  0
            self._u[1]      =  0.05
        elif action == 3:
            # down
            self._u[0]      =  0
            self._u[1]      = -0.05
        else:
            self._u[0]      =  0
            self._u[1]      =  0

        pos, state, reward, done = self.square_world.update(self._u)

        return state, reward, done, {}

    def _reset(self):
        pass

    def _render(self, mode='human', close=False):
        self.square_world.render(close)
