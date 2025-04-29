import random
import pygame
import pygame.freetype


class NPC():
    def __init__(self, character, identity, x, y):
        self.character = pygame.transform.scale(character, (character.get_width()/2.5, character.get_height()/2.5))
        self.identifier = identity
        self.x = x
        self.y = y

    def update(self, wdown, adown, sdown, ddown, walking):
        if wdown:
            self.y += 16
        if adown:
            self.x += 16
        if sdown:
            self.y -= 16
        if ddown:
            self.x -= 16
        if sdown and wdown:
            pass
        elif ddown and adown: 
            pass
        else:
            if wdown and adown:
                self.y -= 4
                self.x -= 4
            if wdown and ddown:
                self.y -= 4
                self.x += 4
            if sdown and adown:
                self.y += 4
                self.x -= 4
            if sdown and ddown:
                self.y += 4
                self.x += 4
        
    def draw(self, surface):
        surface.blit(self.character, (self.x, self.y))

class Spacesea():
    def __init__(self):
        self.sea = pygame.image.load('images\\village\\spacesea.png')
        self.width = self.sea.get_width()
        self.height = self.sea.get_height()
        self.x = -631
        self.y = -2054

    def update(self, wdown, adown, sdown, ddown):
        if wdown:
            self.y += 16
        if adown:
            self.x += 16
        if sdown:
            self.y -= 16
        if ddown:
            self.x -= 16
        if sdown and wdown:
            pass
        elif ddown and adown: 
            pass
        else:
            if wdown and adown:
                self.y -= 4
                self.x -= 4
            if wdown and ddown:
                self.y -= 4
                self.x += 4
            if sdown and adown:
                self.y += 4
                self.x -= 4
            if sdown and ddown:
                self.y += 4
                self.x += 4

    def draw(self, surface):
        surface.blit(self.sea, (self.x, self.y))

class Houseroof():
    def __init__(self, roof, x, y):
        self.roof = pygame.transform.scale(roof, (roof.get_width()/2.5, roof.get_height()/2.5))
        self.x = x
        self.y = y

    def update(self, wdown, adown, sdown, ddown):
        if wdown:
            self.y += 16
        if adown:
            self.x += 16
        if sdown:
            self.y -= 16
        if ddown:
            self.x -= 16
        if sdown and wdown:
            pass
        elif ddown and adown: 
            pass
        else:
            if wdown and adown:
                self.y -= 4
                self.x -= 4
            if wdown and ddown:
                self.y -= 4
                self.x += 4
            if sdown and adown:
                self.y += 4
                self.x -= 4
            if sdown and ddown:
                self.y += 4
                self.x += 4

    def draw(self, surface):
        surface.blit(self.roof, (self.x, self.y))

class Obstructable():
    def __init__(self, base, x, y):
        self.base = pygame.transform.scale(base, (base.get_width()/2.5, base.get_height()/2.5))
        self.x = x
        self.y = y
    
    def update(self, wdown, adown, sdown, ddown):
        if wdown:
            self.y += 16
        if adown:
            self.x += 16
        if sdown:
            self.y -= 16
        if ddown:
            self.x -= 16
        if sdown and wdown:
            pass
        elif ddown and adown: 
            pass
        else:
            if wdown and adown:
                self.y -= 4
                self.x -= 4
            if wdown and ddown:
                self.y -= 4
                self.x += 4
            if sdown and adown:
                self.y += 4
                self.x -= 4
            if sdown and ddown:
                self.y += 4
                self.x += 4

    def draw(self, surface):
        surface.blit(self.base, (self.x, self.y))

class Paths():
    def __init__(self):
        self.background = pygame.image.load('images\\village\\pathsgrass.png')
        self.background = pygame.transform.scale(self.background, (self.background.get_width()/2.5, self.background.get_height()/2.5))
        self.x = -407
        self.y = -1950

    def update(self, wdown, adown, sdown, ddown):
        if wdown:
            self.y += 16
        if adown:
            self.x += 16
        if sdown:
            self.y -= 16
        if ddown:
            self.x -= 16
        if sdown and wdown:
            pass
        elif ddown and adown: 
            pass
        else:
            if wdown and adown:
                self.y -= 4
                self.x -= 4
            if wdown and ddown:
                self.y -= 4
                self.x += 4
            if sdown and adown:
                self.y += 4
                self.x -= 4
            if sdown and ddown:
                self.y += 4
                self.x += 4

    def draw(self, surface):
        surface.blit(self.background, (self.x, self.y))

class Player():

    def __init__(self):
        self.sprite = pygame.image.load('images\\player\\gloopss.png')
        self.sprite = pygame.transform.scale(self.sprite, (self.sprite.get_width()/2.5, self.sprite.get_height()/2.5))
    
    def update(self, wdown, adown, sdown, ddown, lastkey, walking):
        if wdown and not sdown:
            if walking >= 7 and walking <=12:
                self.sprite = pygame.image.load('images\\player\\back1.png')
            elif walking >= 19:
                self.sprite = pygame.image.load('images\\player\\back2.png')
            else:
                self.sprite = pygame.image.load('images\\player\\gloopws.png')
        elif sdown and not wdown:
            if walking >= 7 and walking <=12:
                self.sprite = pygame.image.load('images\\player\\walk1.png')
            elif walking >= 19:
                self.sprite = pygame.image.load('images\\player\\walk2.png')
            else:
                self.sprite = pygame.image.load('images\\player\\gloopss.png')
        elif adown and not ddown:
            if walking >= 7 and walking <=12:
                self.sprite = pygame.image.load('images\\player\\left1.png')
            elif walking >= 19:
                self.sprite = pygame.image.load('images\\player\\left2.png')
            else:
                self.sprite = pygame.image.load('images\\player\\gloopas.png')
        elif ddown and not adown:
            if walking >= 7 and walking <=12:
                self.sprite = pygame.image.load('images\\player\\right1.png')
            elif walking >= 19:
                self.sprite = pygame.image.load('images\\player\\right2.png')
            else:
                self.sprite = pygame.image.load('images\\player\\gloopds.png')
        elif adown and ddown:
            self.sprite = pygame.image.load('images\\player\\gloopss.png')
        elif wdown and sdown:
            self.sprite = pygame.image.load('images\\player\\gloopss.png')
        elif lastkey == "w":
            self.sprite = pygame.image.load('images\\player\\gloopws.png')
        elif lastkey == "a":
            self.sprite = pygame.image.load('images\\player\\gloopas.png')
        elif lastkey == "d":
            self.sprite = pygame.image.load('images\\player\\gloopds.png')
        else:
            self.sprite = pygame.image.load('images\\player\\gloopss.png')
        self.sprite = pygame.transform.scale(self.sprite, (self.sprite.get_width()/2.5, self.sprite.get_height()/2.5))


    def draw(self, surface, displayInfo):
        surface.blit(self.sprite, (int((displayInfo.current_w/2)-(self.sprite.get_width()/2)), int((displayInfo.current_h/2)-(self.sprite.get_height()/2))))

def main():
    pygame.init()
    pygame.display.set_caption("Edge of the World")
    clock = pygame.time.Clock()
    dt = 0
    res = (1920, 1020)
    screen = pygame.display.set_mode(res, pygame.RESIZABLE)
    player, background, spacesea, house1base, house2base, house3base, house1roof, house2roof, house3roof, rail1, rail2, tomato, markiplier, furret, deity = obj_creation()
    keydown = ""
    lastkey = ""
    wdown = False
    adown = False
    sdown = False
    ddown = False
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
        wdown, adown, sdown, ddown, lastkey = get_keydown(lastkey)
        # Game Logic
        walking += 1
        if walking >= 25:
            walking = 0
        displayInfo = pygame.display.Info()
        upd_code(wdown, adown, sdown, ddown, lastkey, walking, spacesea, background, house1base, house2base, house3base, rail1, rail2, player, house1roof, house2roof, house3roof, tomato, markiplier, furret, deity)
        # Render and Display
        draw_objects(screen, black, displayInfo, spacesea, background, house1base, house2base, house3base, rail1, rail2, player, house1roof, house2roof, house3roof, tomato, markiplier, furret, deity)
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
    tomato = NPC(pygame.image.load('images\\tomato\\tomat.png'), "tomato", -199, -398)
    markiplier = NPC(pygame.image.load('images\\markiplier\\mark.png'), "mark", 2145, -1446)
    furret = NPC(pygame.image.load('images\\furret\\furret1.png'), "furret", 2401, -1062)
    deity = NPC(pygame.image.load('images\\deity.png'), "deity", -100, -2000)

    return player, background, spacesea, house1base, house2base, house3base, house1roof, house2roof, house3roof, rail1, rail2, tomato, markiplier, furret, deity

def upd_code(wdown, adown, sdown, ddown, lastkey, walking, spacesea, background, house1base, house2base, house3base, rail1, rail2, player, house1roof, house2roof, house3roof, tomato, markiplier, furret, deity):
    spacesea.update(wdown, adown, sdown, ddown)
    background.update(wdown, adown, sdown, ddown)
    house1base.update(wdown, adown, sdown, ddown)
    house2base.update(wdown, adown, sdown, ddown)
    house3base.update(wdown, adown, sdown, ddown)
    rail1.update(wdown, adown, sdown, ddown)
    rail2.update(wdown, adown, sdown, ddown)
    tomato.update(wdown, adown, sdown, ddown, walking)
    markiplier.update(wdown, adown, sdown, ddown, walking)
    furret.update(wdown, adown, sdown, ddown, walking)
    deity.update(wdown, adown, sdown, ddown, walking)
    player.update(wdown, adown, sdown, ddown, lastkey, walking)
    house1roof.update(wdown, adown, sdown, ddown)
    house2roof.update(wdown, adown, sdown, ddown)
    house3roof.update(wdown, adown, sdown, ddown)

def draw_objects(screen, black, displayInfo, spacesea, background, house1base, house2base, house3base, rail1, rail2, player, house1roof, house2roof, house3roof, tomato, markiplier, furret,deity):
    screen.fill(black)
    spacesea.draw(screen)
    background.draw(screen)
    house1base.draw(screen)
    house2base.draw(screen)
    house3base.draw(screen)
    rail1.draw(screen)
    rail2.draw(screen)
    tomato.draw(screen)
    markiplier.draw(screen)
    furret.draw(screen)
    deity.draw(screen)
    player.draw(screen, displayInfo)
    house1roof.draw(screen)
    house2roof.draw(screen)
    house3roof.draw(screen)

def get_keydown(lastkey):
    pressed = pygame.key.get_pressed()
    keydown=""
    lastkey = lastkey
    wdown = False
    adown = False
    sdown = False
    ddown = False
    if pressed[pygame.K_w]:
        wdown = True
        lastkey = "w"
    if pressed[pygame.K_a]:
        adown = True
        lastkey = "a"
    if pressed[pygame.K_s]:
        sdown = True
        lastkey = "s"
    if pressed[pygame.K_d]:
        ddown = True
        lastkey = "d"
    return wdown, adown, sdown, ddown, lastkey

def start_music():
    pygame.mixer.music.load('audio\\astoryabouttheendoftheworld.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

if __name__ == "__main__":
    main()