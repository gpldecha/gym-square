from gym.envs.registration import register

register(
    id='square-v0',
    entry_point='gym_square.envs:SquareEnv',
    timestep_limit=1000,
)
