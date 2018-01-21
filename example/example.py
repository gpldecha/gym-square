import gym
import gym_square
from time import sleep

env = gym.make('square-v0')

env.square_world.set_agent_state(80)

env.render()
for _ in range(500):

    env.render()
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)

    if done:
        print('Episode finished')
        break

    sleep(0.25)
