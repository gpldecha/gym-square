import sys, pygame
import math
import numpy as np


from grid import Grid
from agent import Agent
import reward as re


class SquareWorld:

    def __init__(self,num_bins=10,reward=re.get_default_reward()):

        self.length     = 10
        self.bRender    = False

        self.reward     = reward
        self.grid       = Grid(length=self.length,num_bins=num_bins)
        self.agent      = Agent(radius=(self.grid.cell_size / 2.0))

    def init_render(self):
        size = 800, 800
        self.screen = pygame.display.set_mode(size)
        pygame.font.init()
        default_font = pygame.font.get_default_font()

        min_size            = min((self.screen.get_width(),self.screen.get_height()))
        self.sq_px_length   = min_size - (2 * 0.1 * min_size)
        self.sq_pos         = 0.1 * min_size
        self.border_color   = (0,0,0)
        self.border_width   = 5
        self.scale          = self.sq_px_length / self.length

        # initialise grid rendering
        self.grid.init_render(screen=self.screen,scale=self.scale,sq_pos=self.sq_pos)

        # initialise agent rendering
        self.agent.init_render(scale=self.scale)

        self.bRender        = True

    def get_observation_space(self):
        """ All Discrete states id with indicies (i,j)
            Returns
                (numpy.ndarray) : N x 3
                                 [:,0]   : state id
                                 [:,1:2] : indices (i,j)
        """
        return self.grid.states

    def update(self,u):
        """ Upates the position of the agent in the square world

            Args:
                u       (numpy.ndarray) : 2D motion vector
            Returns:
                state   (numpy.ndarray) : current state
                reward  (float)         : numerical reward
                done    (bool)          : if episode is finished or not
        """

        # agent motion check that it is valid
        pos        = self.agent.pos + u
        pos        = self.grid.pt2grid(x=pos[0],y=pos[1])
        state      = self.grid.grid2state(i=pos[0],j=pos[1])
        self.agent.update(pos)

        # get the reward
        reward, done = self.reward.R(state=state)

        return pos, state, reward, done


    def render(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        self.screen.fill( (255, 255, 255) )

        pygame.draw.rect(self.screen, self.border_color, (self.sq_pos,self.sq_pos,self.sq_px_length,self.sq_px_length), self.border_width)
        self.grid.draw(self.screen)
        self.agent.draw(self.screen,self.grid.grid2pixel_pos)

        pygame.display.flip()
