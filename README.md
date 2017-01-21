# gym-square
[![Build Status](https://travis-ci.org/gpldecha/gym-square.svg?branch=master)](https://travis-ci.org/gpldecha/gym-square)

A simple square environment for [openai-gym](https://gym.openai.com/).

<p align="left">
  <img src="./docs/square_world.gif" alt="square_world" height="350" >
</p>

# Installation

Clone or download gym-square and cd to the directory.

```bash
$ sudo -H pip install .
```
it will be then installed to ```/usr/local/lib/python2.7/dist-packages/```

# Quick Example

```python
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
        print 'Episode finished'
        break

    sleep(0.25)
```

# Examples 


