import math
import pygame
import numpy as np
import sys

class Agent:

    def __init__(self,radius,pos=[0,0],theta=0):
        self.theta      = theta
        self.pos        = np.array(pos)
        self.pos_tmp    = np.array(pos)
        self.radius     = radius
        self.heading    = np.array([math.cos(theta), math.sin(theta)])


        self._end_pos   = np.array([0,0])
        self._disp      = np.array([0,0])

    def init_render(self,scale):
        self.agent_radius_px  = int(self.radius * scale)


    def update(self,pos):
        if np.sum(pos - self.pos) != 0:
            self.pos_tmp    = self.pos[:]
            self.pos        = pos

            self._disp      = self.pos - self.pos_tmp
            self._disp      = self._disp / ( np.sqrt(np.sum(self._disp**2)) + 0.00001 )
            self.theta      = math.atan2(self._disp[1],self._disp[0])

    def draw(self,screen,grid2pixel_pos):

        pos_agent_px      = grid2pixel_pos(x=self.pos[0],y=self.pos[1])

        self.heading      = 0.5 * np.array([ math.cos(self.theta),math.sin(self.theta)])
        self._end_pos     = self.pos + self.heading

        end_pos_px        = grid2pixel_pos(self._end_pos[0],self._end_pos[1])

        pygame.draw.circle(screen, (255,165,0), pos_agent_px, self.agent_radius_px, 0)
        pygame.draw.line(screen, (0,0,0), pos_agent_px, end_pos_px, 5)
