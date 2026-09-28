import pygame, time
WIDTH,HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
snake = [0]*3
clock = pygame.time.Clock()
#snake body and head
class obj:
    def __init__(self, pos,vel):
        self.pos = pygame.Vector2(pos[0],pos[1])
        self.vel = vel
    def draw(self, screen):
        pygame.draw.rect(screen,(0,255,0),(self.pos[0],self.pos[1],20,20))

for i in range(3):
    snake[i] = obj((WIDTH//2-i*20,HEIGHT//2),20)

#Snake's head direction
def turn(d):
    if d =="U":
        snake[0].pos[1] -= snake[0].vel
    elif d =="D":
        snake[0].pos[1] += snake[0].vel
    elif d =="R":
        snake[0].pos[0] += snake[0].vel
    else:
        snake[0].pos[0] -= snake[0].vel 
    
#update snake body
def update(snake):
    for i in range(len(snake)-1,0,-1):
        snake[i].pos = pygame.Vector2(snake[i-1].pos[0],snake[i-1].pos[1])
#Game
direction = None
running = True
timer = 0
x =0
while running:
    dt = clock.tick(60)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = 'R'
            if event.key == pygame.K_LEFT:
                direction = 'L'
            if event.key == pygame.K_UP:
                direction = 'U'
            if event.key == pygame.K_DOWN:
                direction = 'D'
    timer += dt
    if direction != None and timer >=0.3 and x ==0:
        x =1
        timer=0
        update(snake)
        turn(direction)
        for i in snake:
            print(i.pos)
        
    screen.fill((0,0,0))
    for piece in snake:
        piece.draw(screen)
    pygame.display.flip()
pygame.quit()