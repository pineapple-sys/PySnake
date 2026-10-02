import pygame, time, random
WIDTH,HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
snake = [0]*3
apples = [0]*1
clock = pygame.time.Clock()
#snake body and head
class obj:
    def __init__(self, pos,vel,rgb):
        self.pos = pygame.Vector2(pos[0],pos[1])
        self.vel = vel
        self.rgb = rgb
    def draw(self, screen):
        pygame.draw.rect(screen,self.rgb,(self.pos[0],self.pos[1],20,20))

for i in range(3):
    snake[i] = obj((WIDTH//2-i*20,HEIGHT//2),20,(0,255,0))


#apple
def apple(snake):
    a_pos = None
    while a_pos == None:
        w = random.randrange(0,WIDTH-20,20)
        h = random.randrange(0,HEIGHT-20,20)
        for i in snake:
            if (w +20 >= i.pos[0] and
            w <= i.pos[0]+20 and
            h +20 >= i.pos[1] and
            h <= i.pos[1]+20):
                a_pos = None
                break
            else:
                a_pos = (w,h)
                return(a_pos)
for i in range(1):
    apples[i]= obj(apple(snake),20,(255,0,0))
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
    if direction != None and timer >=0.2:
        timer=0
        update(snake)
        turn(direction)
    if not apples:
        for i in range(1):
            apples[i]= obj(apple(snake),20)
    screen.fill((0,0,0))
    for piece in snake:
        piece.draw(screen)
    for a in apples:
        a.draw(screen)
    pygame.display.flip()
pygame.quit()
