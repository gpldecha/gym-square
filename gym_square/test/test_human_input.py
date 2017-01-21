import unittest
import gym

from gym_square.envs.square_env import SquareEnv
from gym_square.envs.square_world.keyboard import Keyboard

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

        #keyboard = Keyboard()

        #env.render()
        for i in range(1):
        #    env.render()

            action = 0 # keyboard.get_action()
            observation, reward, done, info = env.step(action)

            print 'i:    ', i
            print 'act:  ', action
            print 'obs:  ', observation
            print 'rew:  ', reward
            print 'done: ', done
            print ' '

            if done:
                print 'Episode Finished'
                break

        return True


if __name__ == '__main__':
    unittest.main()
