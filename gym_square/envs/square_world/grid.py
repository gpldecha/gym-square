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

    def init_render(self,screen,scale,sq_pos):

        # colors
        self.black          = (0,0,0)
        self.scale          = scale

        self.width          = screen.get_width()
        self.height         = screen.get_height()
        self.offset         = (self.cell_size / 2.0) * self.scale
        self.sq_pos         = sq_pos

        default_font        = pygame.font.get_default_font()
        self.font_renderer  = pygame.font.Font(default_font, 20)

        self.pts_px     = []
        for x in self.pts:
            start_pos       = [self.scale * (x - self.length / 2.0),  self.scale * (0 - self.length / 2.0)]
            end_pos         = [self.scale * (x - self.length / 2.0),  self.scale * (self.length - self.length / 2.0)]
            start_pos_px    = self.world2pixel_pos(x=start_pos[0],y=start_pos[1])
            end_pos_px      = self.world2pixel_pos(x=end_pos[0],y=end_pos[1])
            self.pts_px.append([start_pos_px,end_pos_px])
        self.pts_py     = []
        for y in self.pts:
            start_pos       = [self.scale * (0 - self.length / 2.0),          self.scale * (y - self.length / 2.0)]
            end_pos         = [self.scale * (self.length - self.length / 2.0),     self.scale * (y - self.length / 2.0)]
            start_pos_py    = self.world2pixel_pos(x=start_pos[0],y=start_pos[1])
            end_pos_py      = self.world2pixel_pos(x=end_pos[0],y=end_pos[1])
            self.pts_py.append([start_pos_py,end_pos_py])

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

    def world2pixel_pos(self,x,y):
        return map(int,[x + self.width/2.0, -y + self.height/2.0])

    def grid2pixel_pos(self,x,y):
        return map(int,[x * self.scale + self.sq_pos + self.offset, -y * self.scale + self.height - self.sq_pos - self.offset])

    def world2pixel_orient(self,orientation):
        return orientation + math.pi / 2.0

    def _draw_states(self,screen):
        for row in self.states:
            text = self.font_renderer.render(str(int(row[0])), 1, self.black)
            text_w = text.get_rect().width
            text_h = text.get_rect().height
            pos = self.grid2pixel_pos(row[1],row[2])
            screen.blit(text, [pos[0] - text_w/2,pos[1] - text_h/2])

    def draw(self,screen):
        for px in self.pts_px:
            pygame.draw.line(screen, self.black, px[0], px[1], 2)
        for py in self.pts_py:
            pygame.draw.line(screen, self.black, py[0], py[1], 2)

        self._draw_states(screen=screen)
