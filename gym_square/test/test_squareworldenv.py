import unittest
import gym

from gym_square.envs.square_env import SquareEnv
from time import sleep
import numpy as np
import matplotlib.cm as cmx


class TestSquareWorldEnv(unittest.TestCase):

    def test_square_world_disc_env(self):

        env = SquareEnv()
        env.reset()

        env.square_world.set_agent_state(55)

        cm = cmx.get_cmap('brg')
        env.square_world.reward.set_color_map(cm)

        for _ in range(1):

            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)

            if done:
                print('Episode Finished')
                break

            sleep(0.001)

        return True


if __name__ == '__main__':
    unittest.main()
