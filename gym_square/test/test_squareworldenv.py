import unittest
import gym

from gym_square.envs.square_env import SquareEnv
from time import sleep


class TestLeftRightEnv(unittest.TestCase):

    def test_env(self):

        env = SquareEnv()
        env.reset()
        for _ in range(100):

            env.render()
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

            sleep(0.2)

        for _ in range(1):
            env.render()
            sleep(0.2)


        return True


if __name__ == '__main__':
    unittest.main()
