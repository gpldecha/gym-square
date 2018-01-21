import gym
import gym_square
from gym_square.envs.square_world.keyboard import Keyboard
from time import sleep

env = gym.make('square-v0')

env.square_world.set_agent_state(80)
env.render()

keyboard = Keyboard()

for _ in range(500):

    env.render()
    action = keyboard.get_action()
    observation, reward, done, info = env.step(action)

    if done:
        print('Episode Finished')
        break
