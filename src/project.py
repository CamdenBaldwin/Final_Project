import random
import pygame
import pygame.freetype

class Text():
    def __init__(self, character, x, y):
        self.character = character
        self.x = x
        self.y = y
        self.size = 35
        font = self.font = pygame.freetype.SysFont('balatrofontjokerregular', (self.size))
        self.text, self.rect = font.render(self.character, (167,184,214))

    def draw(self, surface):
        surface.blit(self.text, (self.x, self.y))


class Dialogue():
    def __init__(self):
        self.tomtodlg = ["*Wow it's me, Tomato Periscone.", "*I made the music for this game."]
        self.markdlg = ["Hello everybody, my name is Markiplier, and welcome tooo my bridge.", "Watch my movie Iron Lung when it comes out."]
        self.furretdlg = ["...", ".....", "...........", "...............", "I walk", 0, ":D"]
        self.tomtoitrt = 0
        self.markitrt = 0
        self.furretitrt = 0
        self.char = 0
        self.dlg = []

    def update(self, speaking, surface, npc):
        self.x = 100
        self.y = 80
        self.speaking = speaking
        self.npc = npc
        if self.npc == "tomato":
            for char in self.tomtodlg[self.tomtoitrt]:
                if self.x > 1600:
                    self.x = 0
                    self.y += 50
                text = Text(char, self.x, self.y)
                self.dlg.insert(0, text)
                self.draw(surface)
                self.char += 1
                self.x += 40
            if self.tomtoitrt<len(self.tomtodlg)-1:
                self.tomtoitrt += 1
        elif self.npc == "mark":
            self.dlg = self.tomtodlg
        elif self.npc == "furret":
            self.dlg = self.tomtodlg

    def draw(self, surface):
        self.dlg[0].draw(surface)
            

class DialogueBubble():
    def __init__(self):
        self.box = pygame.image.load('images\\dialogue\\dialoguebubble.png')
        self.img_ratio = self.box.get_width()/self.box.get_height()
        self.x = 0
        self.y = 0
        self.music = False
        self.fade = (0, 0, 0, 200)
        self.dialogue = Dialogue()
        
    def update(self, playerrect, tomatorect, markrect, furretrect, speaking, displayInfo, walking, iterate):
        self.bgsurf = pygame.Surface((displayInfo.current_w, displayInfo.current_h), pygame.SRCALPHA)
        self.playerrect = playerrect
        self.tomatorect = tomatorect
        self.markrect = markrect
        self.furretrect = furretrect
        self.speaking = speaking
        self.iterate = iterate

        self.dispw = displayInfo.current_w
        self.disph = displayInfo.current_h
        self.w = displayInfo.current_w - (displayInfo.current_w/10)
        self.box = pygame.transform.scale(self.box, (self.w, self.w/self.img_ratio))
        self.x = int((self.dispw/2)-(self.box.get_width()/2))
        self.y = int((self.disph/10*9)-(self.box.get_height()))

        if pygame.Rect.colliderect(self.playerrect, self.tomatorect) and self.speaking:
            self.specnpc = "tomato"
            if self.music == False:
                pygame.mixer.music.fadeout(1000)
                pygame.mixer.music.load('audio\\tomton.mp3')
                pygame.mixer.music.play(-1)
                self.music = True
            self.npc = pygame.image.load('images\\tomato\\tomat.png')
        
        elif pygame.Rect.colliderect(self.playerrect, self.markrect) and self.speaking:
            self.npc = pygame.image.load('images\\markiplier\\mark.png')
        
        elif pygame.Rect.colliderect(self.playerrect, self.furretrect) and self.speaking:
            if self.music == False:
                pygame.mixer.music.fadeout(1000)
                pygame.mixer.music.load('audio\\walk.mp3')
                pygame.mixer.music.play(-1)
                self.music = True
            if walking <= 12: 
                self.npc = pygame.image.load('images\\furret\\furret1.png')
            else:
                self.npc = pygame.image.load('images\\furret\\furret2.png')

    def draw(self, surface):
        if ((pygame.Rect.colliderect(self.playerrect, self.tomatorect) and self.speaking) or (pygame.Rect.colliderect(self.playerrect, self.markrect) 
             and self.speaking) or (pygame.Rect.colliderect(self.playerrect, self.furretrect) and self.speaking)):
            pygame.draw.rect(self.bgsurf, self.fade, self.bgsurf.get_rect())
            surface.blit(self.bgsurf, (0, 0))
            surface.blit(self.npc, (int((self.dispw/2)-(self.npc.get_width()/2)), int((self.disph/2-(self.disph/10))-(self.npc.get_height()/2))))
            surface.blit(self.box, (self.x, self.y))
            if self.iterate == True:
                self.dialogue.update(self.speaking, self.box, self.specnpc)

class Prompt():
    def __init__(self, identity):
        self.prompt = pygame.image.load('images\\dialogue\\eprompt.png')
        self.x = identity.x + (identity.character.get_width() / 2) - (self.prompt.get_width() / 2)
        self.y = identity.y - self.prompt.get_height() - 8

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

    def draw(self, surface, playerrect, npcrect):
        if pygame.Rect.colliderect(playerrect, npcrect):
            surface.blit(self.prompt, (self.x, self.y))

class NPC():
    def __init__(self, character, identity, x, y):
        self.character = pygame.transform.scale(character, (character.get_width()/2.5, character.get_height()/2.5))
        self.identifier = identity
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
        self.x = 0
        self.y = 0
    
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
        self.x = int((displayInfo.current_w/2)-(self.sprite.get_width()/2))
        self.y = int((displayInfo.current_h/2)-(self.sprite.get_height()/2))
        surface.blit(self.sprite, (self.x, self.y))

def main():
    pygame.init()
    pygame.display.set_caption("Edge of the World")
    clock = pygame.time.Clock()
    dt = 0
    res = (1920, 1020)
    screen = pygame.display.set_mode(res, pygame.RESIZABLE)
    (player, background, spacesea, house1base, house2base, house3base, house1roof, house2roof, 
     house3roof, rail1, rail2, tomato, markiplier, furret, deity, tomatoprompt, markprompt, 
     furretprompt, dialogue) = obj_creation()
    playerrect = pygame.Rect(0, 0, 0, 0)
    tomatorect = pygame.Rect(0, 0, 0, 0)
    markrect = pygame.Rect(0, 0, 0, 0)
    furretrect = pygame.Rect(0, 0, 0, 0)
    iterate = False
    speaking = False
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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                if pygame.Rect.colliderect(playerrect, tomatorect) or pygame.Rect.colliderect(playerrect, markrect) or pygame.Rect.colliderect(playerrect, furretrect):
                    iterate = True
                    speaking = True
        wdown, adown, sdown, ddown, lastkey = get_keydown(lastkey, speaking)
        # Game Logic
        walking += 1
        if walking >= 25:
            walking = 0
        displayInfo = pygame.display.Info()
        playerrect, tomatorect, markrect, furretrect = collisions(player, tomato, markiplier, furret)
        upd_code(displayInfo, wdown, adown, sdown, ddown, iterate, lastkey, walking, spacesea, background, house1base, house2base, house3base, rail1, rail2, player, 
                 house1roof, house2roof, house3roof, tomato, markiplier, furret, deity, tomatoprompt, markprompt, furretprompt, playerrect, tomatorect, 
                     markrect, furretrect, dialogue, speaking)
        # Render and Display
        draw_objects(screen, black, displayInfo, spacesea, background, house1base, house2base, house3base, rail1, rail2, player, house1roof, 
                     house2roof, house3roof, tomato, markiplier, furret, deity, tomatoprompt, markprompt, furretprompt, playerrect, tomatorect, 
                     markrect, furretrect, dialogue)
        iterate = False
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
    deity = NPC(pygame.image.load('images\\deity\\deity.png'), "deity", -100, -2000)
    tomatoprompt = Prompt(tomato)
    markprompt = Prompt(markiplier)
    furretprompt = Prompt(furret)
    dialogue = DialogueBubble()

    return (player, background, spacesea, house1base, house2base, house3base, house1roof, house2roof, house3roof, rail1, rail2, tomato, markiplier, 
            furret, deity, tomatoprompt, markprompt, furretprompt, dialogue)

def upd_code(displayInfo, wdown, adown, sdown, ddown, iterate, lastkey, walking, spacesea, background, house1base, house2base, house3base, rail1, rail2, player, house1roof, 
             house2roof, house3roof, tomato, markiplier, furret, deity, tomatoprompt, markprompt, furretprompt, playerrect, tomatorect, markrect, furretrect, 
             dialogue, speaking):
    spacesea.update(wdown, adown, sdown, ddown)
    background.update(wdown, adown, sdown, ddown)
    house1base.update(wdown, adown, sdown, ddown)
    house2base.update(wdown, adown, sdown, ddown)
    house3base.update(wdown, adown, sdown, ddown)
    rail1.update(wdown, adown, sdown, ddown)
    rail2.update(wdown, adown, sdown, ddown)
    tomato.update(wdown, adown, sdown, ddown)
    markiplier.update(wdown, adown, sdown, ddown)
    furret.update(wdown, adown, sdown, ddown)
    deity.update(wdown, adown, sdown, ddown)
    player.update(wdown, adown, sdown, ddown, lastkey, walking)
    house1roof.update(wdown, adown, sdown, ddown)
    house2roof.update(wdown, adown, sdown, ddown)
    house3roof.update(wdown, adown, sdown, ddown)
    tomatoprompt.update(wdown, adown, sdown, ddown)
    markprompt.update(wdown, adown, sdown, ddown)
    furretprompt.update(wdown, adown, sdown, ddown)
    dialogue.update(playerrect, tomatorect, markrect, furretrect, speaking, displayInfo, walking, iterate)

def draw_objects(screen, black, displayInfo, spacesea, background, house1base, house2base, house3base, rail1, rail2, player, house1roof, house2roof, 
                 house3roof, tomato, markiplier, furret, deity, tomatoprompt, markprompt, furretprompt, playerrect, tomatorect, markrect, furretrect, 
                 dialogue):
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
    tomatoprompt.draw(screen, playerrect, tomatorect)
    markprompt.draw(screen, playerrect, markrect)
    furretprompt.draw(screen, playerrect, furretrect)
    dialogue.draw(screen)

def get_keydown(lastkey, speaking):
    pressed = pygame.key.get_pressed()
    keydown=""
    lastkey = lastkey
    wdown = False
    adown = False
    sdown = False
    ddown = False
    if not speaking:
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

def collisions(player, tomato, mark, furret):
    playerrect = pygame.Rect(player.x+16, (player.y+291), player.sprite.get_width()-32, (player.sprite.get_height()/15))
    tomatorect = pygame.Rect(tomato.x - 200, (tomato.y - 200), tomato.character.get_width()+400, tomato.character.get_height()+400)
    markrect = pygame.Rect(mark.x, (mark.y + 100), mark.character.get_width(), mark.character.get_height()+80)
    furretrect = pygame.Rect(furret.x - 100, (furret.y+50), furret.character.get_width()+100, furret.character.get_height()-10)

    return playerrect, tomatorect, markrect, furretrect

def start_music():
    pygame.mixer.music.load('audio\\astoryabouttheendoftheworld.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

if __name__ == "__main__":
    main()