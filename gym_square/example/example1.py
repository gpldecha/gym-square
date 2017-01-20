import gym
import gym_square
from time import sleep

env = gym.make('square-v0')

env.square_world.set_agent_state(80)
env.render()

for _ in range(100):
    env.render()
    sleep(0.1)

for _ in range(500):

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

    sleep(0.25)

env.render()