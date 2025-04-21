import random
import pygame
import pygame.freetype

class Spacesea():
    def __init__(self):
        self.sea = pygame.image.load('images\\village\\spacesea.png')
        self.width = self.sea.get_width()
        self.height = self.sea.get_height()
        self.x = -631
        self.y = -2054

    def update(self, direction):
        if direction == "w":
            self.y += 16
        elif direction == "a":
            self.x += 16
        elif direction == "s":
            self.y -= 16
        elif direction == "d":
            self.x -= 16
        else:
            pass

    def draw(self, surface):
        surface.blit(self.sea, (self.x, self.y))

class Houseroof():
    def __init__(self, roof, x, y):
        self.roof = roof
        self.width = self.roof.get_width()
        self.height = self.roof.get_height()
        self.roof = pygame.transform.scale(self.roof, (self.width/2.5, self.height/2.5))
        self.x = x
        self.y = y

    def update(self, direction):
        if direction == "w":
            self.y += 16
        elif direction == "a":
            self.x += 16
        elif direction == "s":
            self.y -= 16
        elif direction == "d":
            self.x -= 16
        else:
            pass

    def draw(self, surface):
        surface.blit(self.roof, (self.x, self.y))

class Obstructable():
    def __init__(self, base, x, y):
        self.base = base
        self.width = self.base.get_width()
        self.height = self.base.get_height()
        self.base = pygame.transform.scale(self.base, (self.width/2.5, self.height/2.5))
        self.x = x
        self.y = y
    
    def update(self, direction):
        if direction == "w":
            self.y += 16
        elif direction == "a":
            self.x += 16
        elif direction == "s":
            self.y -= 16
        elif direction == "d":
            self.x -= 16
        else:
            pass
    def draw(self, surface):
        surface.blit(self.base, (self.x, self.y))

class Paths():
    def __init__(self):
        self.background = pygame.image.load('images\\village\\pathsgrass.png')
        self.width = self.background.get_width()
        self.height = self.background.get_height()
        self.background = pygame.transform.scale(self.background, (self.width/2.5, self.height/2.5))
        self.x = -407
        self.y = -1950

    def update(self, direction):
        if direction == "w":
            self.y += 16
        elif direction == "a":
            self.x += 16
        elif direction == "s":
            self.y -= 16
        elif direction == "d":
            self.x -= 16
        else:
            pass

    def draw(self, surface):
        surface.blit(self.background, (self.x, self.y))

class Player():

    def __init__(self):
        self.sprite = pygame.image.load('images\\player\\gloopss.png')
    
    def update(self, direction, lastkey, walking):
        if direction == "w":
            if walking >= 7 and walking <=12:
                self.sprite = pygame.image.load('images\\player\\back1.png')
            elif walking >= 19:
                self.sprite = pygame.image.load('images\\player\\back2.png')
            else:
                self.sprite = pygame.image.load('images\\player\\gloopws.png')
        elif direction == "a":
            if walking >= 7 and walking <=12:
                self.sprite = pygame.image.load('images\\player\\left1.png')
            elif walking >= 19:
                self.sprite = pygame.image.load('images\\player\\left2.png')
            else:
                self.sprite = pygame.image.load('images\\player\\gloopas.png')
        elif direction == "s":
            if walking >= 7 and walking <=12:
                self.sprite = pygame.image.load('images\\player\\walk1.png')
            elif walking >= 19:
                self.sprite = pygame.image.load('images\\player\\walk2.png')
            else:
                self.sprite = pygame.image.load('images\\player\\gloopss.png')
        elif direction == "d":
            if walking >= 7 and walking <=12:
                self.sprite = pygame.image.load('images\\player\\right1.png')
            elif walking >= 19:
                self.sprite = pygame.image.load('images\\player\\right2.png')
            else:
                self.sprite = pygame.image.load('images\\player\\gloopds.png')
        elif lastkey == "w":
            self.sprite = pygame.image.load('images\\player\\gloopws.png')
        elif lastkey == "a":
            self.sprite = pygame.image.load('images\\player\\gloopas.png')
        elif lastkey == "d":
            self.sprite = pygame.image.load('images\\player\\gloopds.png')
        else:
            self.sprite = pygame.image.load('images\\player\\gloopss.png')
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
    player, background, spacesea, house1base, house2base, house3base, house1roof, house2roof, house3roof, rail1, rail2 = obj_creation()
    keydown = ""
    lastkey = ""
    black = (0,0,0)
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
        keydown, lastkey = get_keydown(lastkey)
        # Game Logic
        walking += 1
        if walking >= 25:
            walking = 0
        displayInfo = pygame.display.Info()
        upd_code(keydown, lastkey, walking, spacesea, background, house1base, house2base, house3base, rail1, rail2, player, house1roof, house2roof, house3roof)
        # Render and Display
        draw_objects(screen, black, displayInfo, spacesea, background, house1base, house2base, house3base, rail1, rail2, player, house1roof, house2roof, house3roof)
        pygame.display.flip()
        dt = clock.tick(24)
    pygame.mixer.music.unload()
    pygame.quit()

def obj_creation():
    player = Player()
    background = Paths()
    spacesea = Spacesea()
    house1base = Obstructable(pygame.image.load('images\\village\\house1door.png'), -15, -158)
    house2base = Obstructable(pygame.image.load('images\\village\\house2door.png'), 1185, -158)
    house3base = Obstructable(pygame.image.load('images\\village\\house1door.png'), 2033, -150)
    house1roof = Houseroof(pygame.image.load('images\\village\\house1roof.png'), -39, -366)
    house2roof = Houseroof(pygame.image.load('images\\village\\house2roof.png'), 1145, -366)
    house3roof = Houseroof(pygame.image.load('images\\village\\house1roof.png'), 2009, -358)
    rail1 = Obstructable(pygame.image.load('images\\village\\rail1.png'), -399, -526)
    rail2 = Obstructable(pygame.image.load('images\\village\\rail2.png'), 2305, -526)
    return player, background, spacesea, house1base, house2base, house3base, house1roof, house2roof, house3roof, rail1, rail2

def upd_code(keydown, lastkey, walking, spacesea, background, house1base, house2base, house3base, rail1, rail2, player, house1roof, house2roof, house3roof):
    spacesea.update(keydown)
    background.update(keydown)
    house1base.update(keydown)
    house2base.update(keydown)
    house3base.update(keydown)
    rail1.update(keydown)
    rail2.update(keydown)
    player.update(keydown, lastkey, walking)
    house1roof.update(keydown)
    house2roof.update(keydown)
    house3roof.update(keydown)

def draw_objects(screen, black, displayInfo, spacesea, background, house1base, house2base, house3base, rail1, rail2, player, house1roof, house2roof, house3roof):
    screen.fill(black)
    spacesea.draw(screen)
    background.draw(screen)
    house1base.draw(screen)
    house2base.draw(screen)
    house3base.draw(screen)
    rail1.draw(screen)
    rail2.draw(screen)
    player.draw(screen, displayInfo)
    house1roof.draw(screen)
    house2roof.draw(screen)
    house3roof.draw(screen)

def get_keydown(lastkey):
    pressed = pygame.key.get_pressed()
    keydown=""
    lastkey = lastkey
    if pressed[pygame.K_w]:
        keydown = "w"
        lastkey = "w"
    elif pressed[pygame.K_a]:
        keydown = "a"
        lastkey = "a"
    elif pressed[pygame.K_s]:
        keydown = "s"
        lastkey = "s"
    elif pressed[pygame.K_d]:
        keydown = "d"
        lastkey = "d"
    return keydown, lastkey

def start_music():
    pygame.mixer.music.load('audio\\astoryabouttheendoftheworld.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

if __name__ == "__main__":
    main()