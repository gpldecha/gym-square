import math
import pygame
import numpy as np
import sys

class Agent:

    def __init__(self,radius,state,pos=[0,0],theta=0):

        self.radius     = float(radius)
        self.theta      = float(theta)
        self.heading    = np.array([math.cos(theta), math.sin(theta)])

        if state == 'discrete':
                self.pos        = np.array(pos,dtype=int)
                self.pos_tmp    = np.array(pos,dtype=int)
        elif state == 'continuous':
                self.pos        = np.array(pos,dtype=float)
                self.pos_tmp    = np.array(pos,dtype=float)

        self._end_pos   = np.array([0,0],dtype=float)
        self._disp      = np.array([0,0],dtype=float)

    def init_render(self,scale):
        self.agent_radius_px  = int(self.radius * scale)

    def update(self,pos):
        if np.sum(pos - self.pos) != 0:
            self.pos_tmp    = self.pos[:]
            self.pos        = pos

            self._disp      = self.pos - self.pos_tmp
            self._disp      = self._disp / ( np.sqrt(np.sum(self._disp**2)) + 0.00001 )
            self.theta      = math.atan2(self._disp[1],self._disp[0])

    def draw(self,screen,pt2pixel):
        """
            Args:
                screen (object) : pygame screen
                pt2pixel (function) : given a point in world frame
                                      returns the pixel coordinate

        """

        pos_agent_px      = pt2pixel(x=self.pos[0],y=self.pos[1])

        self.heading      = self.radius * np.array([ math.cos(self.theta),math.sin(self.theta)],dtype=float)
        self._end_pos     = self.pos + self.heading

        end_pos_px        = pt2pixel(self._end_pos[0],self._end_pos[1])

        pygame.draw.circle(screen, (255,165,0), pos_agent_px, self.agent_radius_px, 0)
        pygame.draw.line(screen, (0,0,0), pos_agent_px, end_pos_px, 5)
