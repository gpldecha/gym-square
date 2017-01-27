import pygame
from pygame import gfxdraw
import matplotlib.cm as cmx
import matplotlib.colors as colors
import numpy as np

class Reward(object):

    def __init__(self):
        self.max_reward     = 10.0
        self.default_reward = 0.0
        self.min_reward     = 0.0
        self.set_color_map(cmx.get_cmap('jet'))

    def set_color_map(self,cm):
        self.cNorm      = colors.Normalize(vmin=self.min_reward, vmax=self.max_reward)
        self.scalarMap  = cmx.ScalarMappable(norm=self.cNorm, cmap=cm)

    def R(self,state):
        pass

    def draw(self,screen):
        pass


class DiscreteReward(Reward):

    def __init__(self):
        super(DiscreteReward, self).__init__()
        self.dict = dict()

    def add(self,state,value,done):
        """ Adds a reward value and outcome to a state
                Args:
                    state       (int)   : index of state
                    value       (float) : value of reward for this state
                    done        (bool)  : if this is a terminal state
        """
        self.dict.update({state : (value,done)})

    def clear(self):
        self.dict.clear()

    def R(self,state):
        """
            Args:
                state (int) : state index
            Returns:
                float : reward
                bool  : if termination state is reached or not
        """
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

class ContinuousReward(Reward):

    def __init__(self):
        super(ContinuousReward, self).__init__()
        self.bFirst = True

    def R(self,state):
        """
            Args:
                state (numpy.ndarray) : state vector
            Returns:
                float : reward
        """
        if (state[0] >= 0.95) and (state[1] >= 0.95):
            return 0,True
        else:
            return 0.5, False


    def draw(self,screen,pixel2pt,px_start,px_end):
        if self.bFirst:
            num_x = px_end[0] - px_start[0]
            num_y = px_end[1] - px_start[1]

            print num_x, ' x ', num_y, ' = ', num_x * num_y
            self._c     = np.empty((num_x * num_y,4),dtype=int)
            f           = lambda x : int(255.0 * x)

            z = 0
            for i in xrange(    int(px_start[0]),int(px_end[0]+1)   ):
                for j in xrange(    int(px_start[1]),int(px_end[1]+1)   ):
                    self._c[z,:] = map(f,self.scalarMap.to_rgba(self.R(  pixel2pt(i,j)     )[0]))
                    z = z + 1

            print '         z : ', z
            #xv, yv      = np.meshgrid(np.arange(int(px_start[0]), int(px_end[0]+1), 1), np.arange(int(px_start[1]), int(px_end[0]+1), 1))
            #self.pxs    = np.vstack((xv.flatten(), yv.flatten())).T
            #self.pts    = np.empty(self.pxs.shape,dtype=float)
            #i = 0
            #self._pixels = pygame.surfarray.pixels2d(screen)
            #print 'self._pixels[0][0]: ', self._pixels[0][0]
            #print 'self.pts.shape: ', self.pts.shape

            self.bFirst = False
        else:
            pass
