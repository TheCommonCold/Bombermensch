import pygame
import socket

pygame.init()
done = False
is_blue = True
x = 30
y = 30
map_size=[13,13]
square_size=40
screen = pygame.display.set_mode((map_size[0] * square_size, map_size[1] * square_size))
map=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 1, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1],
     [1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

def przeslanko():
    UDP_IP_ADDRESS = "192.168.0.50"
    UDP_PORT_NO = 1234
    Message = b"Hello, Server"
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSock.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT_NO))


clock = pygame.time.Clock()

def draw_map():
    i=0
    for array in map:
        j=0
        for x in array:
            if(x==1):
                pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(i*square_size, j*square_size, square_size, square_size))
            if(x==2):
                pygame.draw.rect(screen, (75, 75, 75),pygame.Rect(i * square_size, j * square_size, square_size, square_size))

            j=j+1
        i=i+1
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 2
    if pressed[pygame.K_DOWN]: y += 2
    if pressed[pygame.K_LEFT]: x -= 2
    if pressed[pygame.K_RIGHT]: x += 2

    screen.fill((100, 100, 100))
    color = (0, 50, 150)
    pygame.draw.circle(screen, color,(x,y),int((square_size/2)*0.8),0)

    draw_map()

    pygame.display.flip()
    clock.tick(60)