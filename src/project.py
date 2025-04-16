import random
import pygame
import pygame.freetype

class Player():

    def __init__(self):
        self.sprite = pygame.image.load('images\player\gloop.png')
    
    def update(self, direction, walking):
        if direction == "w":
            if walking >= 7:
                self.sprite = pygame.image.load('images\player\\back1.png')
            else:
                self.sprite = pygame.image.load('images\player\\back2.png')
        elif direction == "a":
            if walking >= 7:
                self.sprite = pygame.image.load('images\player\left1.png')
            else:
                self.sprite = pygame.image.load('images\player\left2.png')
        elif direction == "s":
            if walking >= 7:
                self.sprite = pygame.image.load('images\player\\walk1.png')
            else:
                self.sprite = pygame.image.load('images\player\\walk2.png')
        elif direction == "d":
            if walking >= 7:
                self.sprite = pygame.image.load('images\player\\right1.png')
            else:
                self.sprite = pygame.image.load('images\player\\right2.png')
        else:
            self.sprite = pygame.image.load('images\player\gloop.png')
        width = self.sprite.get_width()
        height = self.sprite.get_height()
        self.sprite = pygame.transform.scale(self.sprite, (width/2.2, height/2.2))


    def draw(self, surface, displayInfo):
        surface.blit(self.sprite, (int((displayInfo.current_w/2)-(self.sprite.get_width()/2)), int((displayInfo.current_h/2)-(self.sprite.get_height()/2))))

def main():
    pygame.init()
    pygame.display.set_caption("Edge of the World")
    clock = pygame.time.Clock()
    dt = 0
    res = (1920, 1020)
    screen = pygame.display.set_mode(res, pygame.RESIZABLE)
    player = Player()
    keydown = ""
    walking = 0
    start_music()
    running = True
    fullscreen = False
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode(res, pygame.RESIZABLE)
        pressed = pygame.key.get_pressed()
        keydown=""
        if pressed[pygame.K_w]:
            keydown = "w"
        elif pressed[pygame.K_a]:
            keydown = "a"
        elif pressed[pygame.K_s]:
            keydown = "s"
        elif pressed[pygame.K_d]:
            keydown = "d"
        # Game Logic
        walking += 1
        if walking >= 13:
            walking = 0
        displayInfo = pygame.display.Info()
        player.update(keydown, walking)
        # Render and Display
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        player.draw(screen, displayInfo)
        pygame.display.flip()
        dt = clock.tick(12)
    pygame.mixer.music.unload()
    pygame.quit()

def start_music():
    pygame.mixer.music.load('audio\\astoryabouttheendoftheworld.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

if __name__ == "__main__":
    main()