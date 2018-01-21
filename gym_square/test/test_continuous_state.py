import unittest
import gym

from gym_square.envs.square_continuous_state_env import SquareContinuousStateEnv
from time import sleep
import numpy as np
import matplotlib.cm as cmx


class TestSquareContinuousStateEnv(unittest.TestCase):

    def test_continuous_state_env(self):

        print('=== Test SquareContinuousStateEnv ===')

        env = SquareContinuousStateEnv()
        env.reset()

        cm = cmx.get_cmap('brg')
        env.square_world.reward.set_color_map(cm)

        env.square_world.set_agent_state([0.5, 0.5])

        bRender = False

        if bRender: env.render()

        for _ in range(5):
            if bRender: env.render()

            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)

            print('act:  ', action)
            print('obs:  ', observation)
            print('rew:  ', reward)
            print('done: ', done)
            print(' ')

            if done:
                print('Episode Finished')
                break

            if bRender:
                sleep(1)
            else:
                sleep(0.01)

        return True


if __name__ == '__main__':
    unittest.main()
