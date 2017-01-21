import gym
import gym_square
from time import sleep
import matplotlib.cm as cmx

from gym_square.envs.square_world.reward import Reward

env = gym.make('square-v0')

reward = Reward()
reward.default_reward =   -1.0
reward.max_reward     =  100.0
reward.min_reward     = -100.0
reward.set_color_map(cmx.get_cmap('brg'))
reward.add(state=99,value=100.0,done=True)
reward.add(state=50,value=-100.0,done=True)
reward.add(state=51,value=-100.0,done=True)
reward.add(state=52,value=-100.0,done=True)
reward.add(state=53,value=-100.0,done=True)
reward.add(state=40,value=-100.0,done=True)
reward.add(state=41,value=-100.0,done=True)
reward.add(state=42,value=-100.0,done=True)
reward.add(state=43,value=-100.0,done=True)
reward.add(state=30,value=-100.0,done=True)
reward.add(state=31,value=-100.0,done=True)
reward.add(state=32,value=-100.0,done=True)
reward.add(state=33,value=-100.0,done=True)
reward.add(state=34,value=-100.0,done=True)
reward.add(state=35,value=-100.0,done=True)
reward.add(state=36,value=-100.0,done=True)

env.square_world.set_agent_state(55)
env.square_world.set_reward(reward)

env.render()

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

    sleep(0.5)

env.render()
