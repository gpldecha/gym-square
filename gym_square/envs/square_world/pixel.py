

class Pixel:
    """
        Class for transformation between pixel (i,j) and point (x,y) coordinates

                  screen
          (0,0) ------------- (w,0)
            |                   |
            |  (0,l)-----(l,l)  |
        j   | y  | square  |    |
            |    |         |    |
            |  (0,0)-----(l,0)  |
            |        x          |
         (0,h) -------------  (w,h)
                     i

        h : height
        w : width
        l : length

        scale  = (pixel length of square) / l


        Comment: Everything is drawn within the square world. The origin of the
                 square (0,0) is determined by an offset


    """

    def __init__(self,screen,sq_length,sq_px_length,sq_px_pos):
        """
            Args:
                screen      (object) :  pygame object
                sq_length   (float)  :  (l)ength of square
                scale        (float) :  (pixel length of square) / l
                sq_px_length (int)   :  number of pixels along square edge.
                sq_px_pos    (int)   :  square (0,0) -> screen ( sq_px_pos , sq_px_pos + sq_px_length )

        """
        self.w              = int(      screen.get_width()  )
        self.h              = int(      screen.get_height() )
        self.sq_px_pos      = int(      sq_px_pos           )
        self.sq_px_length   = int(      sq_px_length        )
        self.sq_length      = float(    sq_length           )

        self.scale          = float(self.sq_px_length) / float(self.sq_length)
        self.T_y            = self.sq_px_pos + self.sq_px_length


    def pt2pixel(self,x,y):
        """
            Args:
                x, y (float) : points in the square coordinate frame of reference.
            Returns:
                    [in,int] : pixel (i,j) coordinates.
        """
        return map(int,[(x * self.scale) + self.sq_px_pos, (-y * self.scale) + self.T_y])

    def pixel2pt(self,i,j):
        """
            Args:
                i (int) : pixel coordinate along (w)idth.
                j (int) : pixel coordinate along (h)eight.
            Return:
               [float, float] : [x,y] square coordinates
        """
        return map(int,[float(i - self.sq_px_pos) / self.scale, float(self.T_y - j) / self.scale])
