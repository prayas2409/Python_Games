import pygame

window_height = 500 # as we'll have square so height = width hence 1 param is fine
rows = 20
black_color = (0,0,0) # 0 0 0 is for black
white_color = (255,255,255) # 255 255 255 is for white
red_color = (255,0,0)

class Cube:

    def __init__(self,start,color):
        self.pos = start
        self.color = color

    def draw(self,window):
        distance = window_height // rows
        row = self.pos[0]
        col = self.pos[1]
        pygame.draw.rect(window, self.color, (row*distance+1,col*distance+1, distance-2, distance-2))

class Snake:

    def __init__(self, color, pos):
        self.head = Cube(pos,color)

    def draw(self, window):
        self.head.draw(window) # Drawing head of snake in window

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