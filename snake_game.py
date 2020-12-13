import pygame
import random

window_height = 500 # as we'll have square so height = width hence 1 param is fine
rows = 20
black_color = (0,0,0) # 0 0 0 is for black
white_color = (255,255,255) # 255 255 255 is for white
red_color = (255,0,0)
blue_color = (0,0,255)

class Cube:

    def __init__(self,start,color,dirnx=0,dirny=1):
        # Added default direction for Cube it'll move in right direction by default as x=1, y=0
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

    body = []
    turns= {}
    def __init__(self, color, pos):
        self.head = Cube(pos,color)
        # added default direction where snake could move
        self.body.append(self.head)
        self.dirnx = 1
        self.dirny = 0
    
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()
            for _ in keys:
                # Move left so decrease x 
                if keys[pygame.K_LEFT]:
                    self.dirnx, self.dirny = -1,0
                # Move right so increase s
                elif keys[pygame.K_RIGHT]:
                    self.dirnx, self.dirny = 1,0
                # Move up 
                elif keys[pygame.K_UP]:
                    self.dirnx, self.dirny = 0,-1
                # Move down
                elif keys[pygame.K_DOWN]:
                    self.dirnx, self.dirny = 0,1

                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        len_of_snake = len(self.body) 
        # used the variable to type in short
        for index,cube in enumerate(self.body):
            position = cube.pos[:]
            if position in self.turns:
                turn = self.turns[position]
                cube.move(turn[0],turn[1])
                ''' if last index then pop turns because:
                    previous turns should move out else Cube revolves in same space '''
                if index == len_of_snake - 1:               
                    self.turns.pop(position)
        #handling corner conditions
            else:
                if cube.dirnx == -1 and cube.pos[0] <= 0: cube.pos = (rows-1, cube.pos[1]) # left corner
                elif cube.dirnx == 1 and cube.pos[0] >= rows-1: cube.pos = (0,cube.pos[1]) # right corner
                elif cube.dirny == 1 and cube.pos[1] >= rows-1: cube.pos = (cube.pos[0], 0) # top 
                elif cube.dirny == -1 and cube.pos[1] <= 0: cube.pos = (cube.pos[0],rows-1) # bottom
                else: cube.move(cube.dirnx,cube.dirny) # just move normally

    def add_cube(self):
        # get previous block as per it's position we'll add the new block
        tail = self.body[-1]
        # get the direction in which the previous block is moving.
        dx, dy = tail.dirnx, tail.dirny
 
        if dx == 1 and dy == 0: # if moving in right
            self.body.append(Cube((tail.pos[0]-1,tail.pos[1]),red_color))
        elif dx == -1 and dy == 0: # moving left
            self.body.append(Cube((tail.pos[0]+1,tail.pos[1]),red_color))
        elif dx == 0 and dy == 1: 
            self.body.append(Cube((tail.pos[0],tail.pos[1]-1),red_color))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.pos[0],tail.pos[1]+1),red_color))
        # Assign the direction to newly added Cube
        self.body[-1].dirnx = dx    
        self.body[-1].dirny = dy    

    def draw(self, window):
        self.head.draw(window,eyes=True) # Drawing head of snake in window
        len_of_snake = len(self.body)
        # iterate for rest of body as head is at 0th position hence taken 1 for next
        for num_of_snake in range(1,len_of_snake):
            self.body[num_of_snake].draw(window)
            

def draw_grids(max_width,num_of_rows,window):
    size_of_box = max_width // rows # // to get int
    x = y = 0 # initialize x and y to 0
    for _ in range(rows):
        # increasing the x & y axis co-ordinates by size of each Cube
        x = x + size_of_box
        y = y + size_of_box
        # drawing lines from x & y axis till max width to create grid /boxes
        pygame.draw.line(window,white_color,(x,0), (x,max_width)) 
        pygame.draw.line(window,white_color,(0,y), (max_width,y))

def randomSnack(rows, snake):
    positions = snake.body # get the body of snake
    while True:
        # generate randomly snack coordinates
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0: 
            # Checked if randomly generated block is in snakes body so we need to regenerate
            continue
        else:
            return (x,y)

def redraw_window(window):
    # made snake and snack global so as need not pass them a args
    global snake,snack
    window.fill(black_color)
    snake.draw(window)
    snack.draw(window)
    draw_grids(window_height,rows,window)
    pygame.display.update()

def main():
    global snake, snack
    window = pygame.display.set_mode(size=(window_height,window_height)) 
    clock = pygame.time.Clock()
    snake = Snake(red_color,(10,10)) # Send color and default start position 10,10 as x,y for snake head
    snack = Cube(randomSnack(rows, snake), color=blue_color)

    while(True):
        pygame.time.delay(50) # 50 ms delay so that app does not run too fast
        clock.tick(10) # 10 fps, snake moves 10 blocks per sec
        snake.move() # update the snake cordinates
        if snake.body[0].pos == snack.pos:
            # Create a new snack only when current one is taken by snake
            snake.add_cube()
            snack = Cube(randomSnack(rows, snake), color=blue_color)
        redraw_window(window)

main()