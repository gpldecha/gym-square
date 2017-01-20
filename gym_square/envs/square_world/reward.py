

class Reward:

    def __init__(self):
        self.dict = dict()
        self.default_reward = 0

    def clear(self):
        self.dict.clear()

    def add(self,state,value,done):
        """ Adds a reward value and outcome to a state
                Args:
                    state       (int)   : index of state
                    value       (float) : value of reward for this state
                    done        (bool)  : if this is a terminal state
        """
        self.dict.update({state : (value,done)})

    def R(self,state):
        if state in self.dict.keys():
            return self.dict[state][0], self.dict[state][1]
        else:
            return self.default_reward, False


def get_default_reward():
    reward = Reward()
    reward.default_reward = 0
    reward.add(state=99,value=10,done=True)
    return reward
