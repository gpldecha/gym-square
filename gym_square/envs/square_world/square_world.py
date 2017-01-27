import sys, pygame
import math
import numpy as np


from grid import Grid
from agent import Agent
import reward as re
from pixel import Pixel

class SquareWorld:

    def __init__(self,state='discrete',num_bins=10):

        self.bDiscrete_state = True

        if state == 'discrete':
            self.sq_length          = 10
            self.grid               = Grid(length=self.sq_length,num_bins=num_bins)
            self.agent              = Agent(state=state,radius=(self.grid.cell_size / 2.0))
            self.bDiscrete_state    = True

            self.reward             = re.DiscreteReward()
            self.reward.add(state=99,value=10,done=True)

        elif state == 'continuous':
            self.sq_length          = 1.0
            self.agent              = Agent(state=state,radius=(self.sq_length * 0.025))
            self.bDiscrete_state    = False
            self.reward             = re.ContinuousReward()
        else:
            raise Exception('state can only be "discrete" or "continuous" input was: ' + state)


        self._bRender   = False

    def init_render(self):
        if self._bRender == False:
            pygame.init()
            size = 800, 800
            self.screen = pygame.display.set_mode(size)
            pygame.font.init()
            default_font = pygame.font.get_default_font()

            min_size            = min((self.screen.get_width(),self.screen.get_height()))
            self.sq_px_length   = min_size - (2 * 0.1 * min_size)
            self.sq_px_pos      = 0.1 * min_size
            self.border_color   = (0,0,0)
            self.border_width   = 5
            self.scale          = self.sq_px_length / self.sq_length

            self.pixel          = Pixel(screen=self.screen,sq_length=self.sq_length,sq_px_length=self.sq_px_length,sq_px_pos=self.sq_px_pos)
            self.pt2pixel       = self.pixel.pt2pixel

            #  initialise grid rendering
            if self.bDiscrete_state:
                self.grid.init_render(pt2pixel=self.pt2pixel)

            # initialise agent rendering
            self.agent.init_render(scale=self.scale)

            self._bRender        = True

    def get_observation_space(self):
        """ All Discrete states id with indicies (i,j)
            Returns
                (numpy.ndarray) : N x 3
                                 [:,0]   : state id
                                 [:,1:2] : indices (i,j)
        """
        if self.bDiscrete_state:
            return self.grid.states
        else:
            return [0,self.sq_length]

    def set_agent_state(self,state):
        if self.bDiscrete_state:
            i,j = self.grid.state2grid(state)
            self.agent.pos[0] = i
            self.agent.pos[1] = j
        else:
            self.agent.pos[0] = state[0]
            self.agent.pos[1] = state[1]
        self.agent.pos_tmp = self.agent.pos[:]

    def set_reward(self,reward):
        self.reward = reward

    def update(self,u):
        """ Upates the position of the agent in the square world

            Args:
                u       (numpy.ndarray) : 2D motion vector
            Returns:
                state   (numpy.ndarray) : current state
                reward  (float)         : numerical reward
                done    (bool)          : if episode is finished or not
        """

        pos_u      = self.agent.pos + u


        # agent motion check that it is valid
        if self.bDiscrete_state:
            pos         = self.grid.pt2grid(x=pos_u[0],y=pos_u[1])
            state       = self.grid.grid2state(i=pos[0],j=pos[1])
        else:
            pos         = pos_u
            if pos[0] <= 0.0: pos[0] = 0.0
            if pos[0] >= self.sq_length: pos[0] = self.sq_length
            if pos[1] <= 0.0: pos[1] = 0.0
            if pos[1] >= self.sq_length: pos[1] = self.sq_length
            state       = pos

        # update agent position after checking validity
        self.agent.update(pos)

        # get the reward
        reward, done = self.reward.R(state=state)

        return pos, state, reward, done


    def render(self,close=False):

        if self._bRender and close == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            self.screen.fill( (255, 255, 255) )

            if self.bDiscrete_state:
                self.reward.draw(self.screen,self.grid.state2grid,self.grid.grid2pixel_pos,self.scale,self.grid.cell_size)
            else:
                pass
                # not ready to render
                #self.reward.draw(self.screen,self.pixel.pixel2pt,px_start=[self.sq_px_pos,self.sq_px_pos],px_end=[self.sq_px_pos + self.sq_px_length,self.sq_px_pos + self.sq_px_length])

            pygame.draw.rect(self.screen, self.border_color, (self.sq_px_pos,self.sq_px_pos,self.sq_px_length,self.sq_px_length), self.border_width)

            if self.bDiscrete_state:
                self.grid.draw(self.screen)
                self.agent.draw(self.screen,self.grid.grid2pixel_pos)
            else:
                self.agent.draw(self.screen,self.pt2pixel)

            pygame.display.flip()
        elif self._bRender and close:
            self._bRender = False
            pygame.quit()
        elif self._bRender == False and close == False:
            self.init_render()
