import unittest
import gym

from gym_square.envs.square_env import SquareEnv
from time import sleep
import numpy as np
import matplotlib.cm as cmx


class TestLeftRightEnv(unittest.TestCase):

    def test_env(self):

        env = SquareEnv()
        env.reset()

        env.square_world.set_agent_state(55)

        cm = cmx.get_cmap('brg')
        env.square_world.reward.set_color_map(cm)


        for _ in range(200):
            #env.render()

            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)

            print 'act:  ', action
            print 'obs:  ', observation
            print 'rew:  ', reward
            print 'done: ', done
            print ' '

            if done:
                print 'Episode Finished'
                break

            sleep(0.1)

        return True


if __name__ == '__main__':
    unittest.main()
