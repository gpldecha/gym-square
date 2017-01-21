import pygame

import matplotlib.cm as cmx
import matplotlib.colors as colors

class Reward:

    def __init__(self):
        self.dict = dict()
        self.max_reward     = 10.0
        self.default_reward = 0.0
        self.min_reward     = 0.0

        self.set_color_map(cmx.get_cmap('jet'))

    def set_color_map(self,cm):
        self.cNorm      = colors.Normalize(vmin=self.min_reward, vmax=self.max_reward)
        self.scalarMap  = cmx.ScalarMappable(norm=self.cNorm, cmap=cm)

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


    def draw(self,screen,state2grid,grid2pixel_pos,scale,cell_size):

        for state in self.dict:
            i,j = state2grid(state)

            #                                 left-right                    up-down
            sq_bl_pos = grid2pixel_pos(i - cell_size / 2.0 + (0.02 * cell_size),j + cell_size / 2.0 - (0.02 * cell_size) )

            length = scale * (cell_size - 0.01 * cell_size)

            c = self.scalarMap.to_rgba(self.dict[state][0])
            pygame.draw.rect(screen, (c[0] * 255,c[1] * 255,c[2] * 255), (sq_bl_pos[0],sq_bl_pos[1],length,length),0)



def get_default_reward():
    reward = Reward()
    reward.default_reward   = 0
    reward.min_reward       = 0
    reward.max_reward       = 10
    reward.add(state=99,value=10,done=True)
    return reward
