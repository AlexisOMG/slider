import sys, math, pygame
from constants import *

pygame.init()
screen = pygame.display.set_mode((width, height))
fpclock = pygame.time.Clock()
x, y = 0, 0
clicked = False
def angle(x1, y1, x2, y2):
    angle = ((math.atan2(x1 - x2, y1 - y2) * (180 / math.pi)) + 90) % 360
    return angle
    

def proccess_events():
    global clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x1, y1 = pygame.mouse.get_pos()
            dg = angle(width // 2, height // 2, x1, y1)
            xPos, yPos = math.cos(dg * (math.pi / 180)) * 100, math.sin(dg * (math.pi / 180)) * 100
            if ((int(xPos) + width // 2 - x1) ** 2 + (-1 * int(yPos) + height // 2 - y1) ** 2) ** 0.5 <= 20: 
                clicked = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            clicked = False
            

def main():
    global screen, x, y, fpclock, clicked
    while True:
        screen.fill(white)
        proccess_events()
        if clicked:
            x, y = pygame.mouse.get_pos()
        dg = angle(width // 2, height // 2, x, y)
        pygame.draw.circle(screen, red, (width // 2, height // 2), 100, 2)
        xPos, yPos = math.cos(dg * (math.pi / 180)) * 100, math.sin(dg * (math.pi / 180)) * 100
        pygame.draw.circle(screen, red, (int(xPos) + width // 2, -1 * int(yPos) + height // 2), 20)
        pygame.display.update()
        fpclock.tick(30)
    
if __name__ == "__main__":
    main()
