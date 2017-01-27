import sys, pygame
import math
import numpy as np

class Grid:

    def __init__(self,length,num_bins=10):
        self.pts        = np.linspace(0,length,num_bins,False)
        self.cell_size  = self.pts[1] - self.pts[0]
        self.pts        = self.pts[1:]

        self.num_bins   = num_bins
        self.length     = length

        # compute all states
        self.states = np.empty([self.num_bins * self.num_bins,3])
        idx = 0
        for i in range(0,self.num_bins):
            for j in range(0,self.num_bins):
                self.states[idx,:] = np.array([self.grid2state(i,j),i,j])
                idx=idx+1

    def init_render(self,pt2pixel):

        # colors
        self.black          = (0,0,0)

        self.pt2pixel       = pt2pixel

        default_font        = pygame.font.get_default_font()
        self.font_renderer  = pygame.font.Font(default_font, 20)

        self.pts_px     = []
        for x in self.pts:
            self.pts_px.append([pt2pixel(x=x,y=0),pt2pixel(x=x,y=self.length)])
        self.pts_py     = []
        for y in self.pts:
            self.pts_py.append([pt2pixel(x=0,y=y),pt2pixel(x=self.length,y=y)])

    def pt2grid(self,x,y):
        """ x and y are in the grid's frame of reference which is at
            the bottom left corner of the square.
        """
        if x < 0: x = 0
        if x >= self.length: x = self.length - self.cell_size
        if y < 0: y = 0
        if y >= self.length: y = self.length - self.cell_size

        x = round( (float(x) / float(self.length)) * float(self.num_bins))
        y = round( (float(y) / float(self.length)) * float(self.num_bins))

        return np.array([x,y])

    def grid2state(self,i,j):
        """ i and j are integer coordinates, returns a state coordinate """
        return int(j * self.num_bins + i)

    def state2grid(self,state):
        return float(state) % float(self.num_bins), int(float(state) / float(self.num_bins))

    def grid2pixel_pos(self,x,y):
        return self.pt2pixel(x=(x + self.cell_size / 2.0),y=(y + self.cell_size / 2.0))

    def _draw_states(self,screen):
        for row in self.states:
            text = self.font_renderer.render(str(int(row[0])), 1, self.black)
            text_w = text.get_rect().width
            text_h = text.get_rect().height
            pos = self.pt2pixel(x=(row[1] + self.cell_size / 2.0),y=(row[2]+ self.cell_size / 2.0))
            screen.blit(text, [pos[0] - text_w/2,pos[1] - text_h/2])

    def draw(self,screen):
        for px in self.pts_px:
            pygame.draw.line(screen, self.black, px[0], px[1], 2)
        for py in self.pts_py:
            pygame.draw.line(screen, self.black, py[0], py[1], 2)

        self._draw_states(screen=screen)
