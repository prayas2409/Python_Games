import pygame

window_height = 500 # as we'll have square so height = width hence 1 param is fine
rows = 20
black_color = (0,0,0) # 0 0 0 is for black
white_color = (255,255,255) # 255 255 255 is for white
red_color = (255,0,0)

class Cube:

    def __init__(self,start,color,dirnx=0,dirny=1):
        # Added default direction for cube it'll move in right direction by default as x=1, y=0
        self.pos = start
        self.color = color
        self.dirnx = dirnx
        self.dirny = dirny

    def draw(self,window, eyes=False):
        # eyes as true/false only for head it'll be sent true and for rest body it's false
        distance = window_height // rows
        row = self.pos[0]
        col = self.pos[1]
        pygame.draw.rect(window, self.color, (row*distance+1,col*distance+1, distance-2, distance-2))

        if eyes:
            #only if eyes provided i.e for head, draw eyes else plain red block
            centre = distance // 2
            radius = 3
            # x and y axis for eye1 and eye2 of snake
            eye_one = (row*distance+centre-radius,col*distance+8)
            eye_two = (row*distance + distance -radius*2, col*distance+8)
            # Drawing actual eyes
            pygame.draw.circle(window, black_color, eye_one, radius)
            pygame.draw.circle(window, black_color, eye_two, radius)

    def move(self,dirnx,dirny):
        # getting directions and updating the position
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

class Snake:

    def __init__(self, color, pos):
        self.head = Cube(pos,color)
        # added default direction where snake could move
        self.dirnx = 1
        self.dirny = 0
    
    def move(self):
        # used the variable to type in short
        cube = self.head

        #handling corner conditions
        if cube.dirnx == -1 and cube.pos[0] <= 0: cube.pos = (rows-1, cube.pos[1]) # left corner
        elif cube.dirnx == 1 and cube.pos[0] >= rows-1: cube.pos = (0,cube.pos[1]) # right corner
        elif cube.dirny == 1 and cube.pos[1] >= rows-1: cube.pos = (cube.pos[0], 0) # top 
        elif cube.dirny == -1 and cube.pos[1] <= 0: cube.pos = (cube.pos[0],rows-1) # bottom
        else: cube.move(cube.dirnx,cube.dirny) # just move normally

    def draw(self, window):
        self.head.draw(window,eyes=True) # Drawing head of snake in window

def draw_grids(max_width,num_of_rows,window):
    size_of_box = max_width // rows # // to get int
    x = y = 0 # initialize x and y to 0
    for _ in range(rows):
        # increasing the x & y axis co-ordinates by size of each cube
        x = x + size_of_box
        y = y + size_of_box
        # drawing lines from x & y axis till max width to create grid /boxes
        pygame.draw.line(window,white_color,(x,0), (x,max_width)) 
        pygame.draw.line(window,white_color,(0,y), (max_width,y))

snake = Snake(red_color,(10,10)) # Send color and start position as x,y for snake head

def redraw_window(window):
    window.fill(black_color)
    snake.move() # update the snake cordinates
    snake.draw(window)
    draw_grids(window_height,rows,window)
    pygame.display.update()

def main():
    window = pygame.display.set_mode(size=(window_height,window_height)) 
    clock = pygame.time.Clock()
    while(True):
        pygame.time.delay(50) # 50 ms delay so that app does not run too fast
        clock.tick(10) # 10 fps, snake moves 10 blocks per sec
        redraw_window(window)
        
main()