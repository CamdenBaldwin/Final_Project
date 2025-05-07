import pygame
import pygame.freetype

class Rectangle():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.rectangle = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, wdown, adown, sdown, ddown, colliding, skipy = False, skipx = False):
        if colliding == False:
            self.priorx = self.x
            self.priory = self.y
            self.x, self.y = upd_pos(self.x, self.y, wdown, adown, sdown, ddown)
            self.rectangle = pygame.Rect(self.x, self.y, self.width, self.height)
        elif colliding == True:
            if skipx:
                self.x = self.priorx
                if wdown:
                    self.y += 4
                if sdown: 
                    self.y -= 4
            if skipy:
                self.y = self.priory
                if adown:
                    self.x += 4
                if ddown: 
                    self.x -= 4
            self.rectangle = pygame.Rect(self.x, self.y, self.width, self.height)

class Text():
    def __init__(self, word, x, y):
        self.word = word
        self.x = x
        self.y = y
        self.size = 35
        self.font = pygame.freetype.SysFont('balatrofontjokerregular', (self.size))
        self.text, self.rect = self.font.render(self.word, (167,184,214))
        self.text_width = self.text.get_width()
        self.text_height = self.text.get_height()

    def draw(self, surface):
        surface.blit(self.text, (self.x, self.y))

class Dialogue():
    def __init__(self):
        self.tomtodlg = [["*i ", "am ", "john ", "deltarune"], ["*ur ", "ur ", "ur ", "ur ", "ur ", "ur ", "ur"], 0 , 
                         ["*ur ", "ur ", "ur ", "ur ", "ur ", "ur ", "ur"], ["*john ", "deltarune"], 0, ["*SOMEBODY, ", "STOP ", "ME!!!"], 
                         ["*I'M ", "SMOKING ", "THE ", "TRACK!!!!!!!"], ["*I'LL ", "GIGGITY ", "LOIS... "], ["*AND ", "MAKE ", "MORE ", "SONS ", "OF ", "THE ", "MASK!!!!!!!!!!"],
                         0, ["*Dialogue ", "courtesy ", "of ", "tomato, ", "she ", "also ", "made ", "the ", "music ", ":)"]]
        self.markdlg = [["Hello ", "everybody, ", "my ", "name ", "is ", "Markiplier, ", "and ", "welcome ", "tooo ", "my ", "bridge."], 
                        ["Watch ", "my ", "movie ", "'Iron ", "Lung '", "when ", "it ", "comes ", "out."]]
        self.furretdlg = [["..."], ["....."], ["..........."], ["..............."], ["I ", "walk"], 0, [":D"]]
        self.tomtoitrt = 0
        self.markitrt = 0
        self.furretitrt = 0
        self.char = 0
        self.dlg = []

    def update(self, speaking, npc):
        self.x = 200
        self.y = 670
        self.speaking = speaking
        self.npc = npc
        if self.npc == "tomato":
            self.dlg = []
            for word in self.tomtodlg[self.tomtoitrt]:
                self.word = word
                self.update_text()
            if self.tomtoitrt <= len(self.tomtodlg):
                self.tomtoitrt += 1
        elif self.npc == "mark":
            self.dlg = []
            for word in self.markdlg[self.markitrt]:
                self.word = word
                self.update_text()
            if self.markitrt <= len(self.markdlg):
                self.markitrt += 1
        elif self.npc == "furret":
            self.dlg = []
            for word in self.furretdlg[self.furretitrt]:
                self.word = word
                self.update_text()
            if self.furretitrt <= len(self.furretdlg):
                self.furretitrt += 1

    def update_text(self):
        text = Text(self.word, self.x, self.y)
        if self.x + text.text_width > 1600:
            text.x = 200
            self.x = 200
            text.y += text.text_height + 20
            self.y += text.text_height + 20
        self.dlg.insert(0, text)
        self.char += 1
        self.x += text.text_width + 10

    def draw(self, surface):
        self.dlg[0].draw(surface)
        for character in self.dlg:
            character.draw(surface)
           
class DialogueBubble():
    def __init__(self):
        self.box = pygame.image.load('images\\dialogue\\dialoguebubble.png')
        self.img_ratio = self.box.get_width()/self.box.get_height()
        self.button = pygame.image.load('images\\dialogue\\ebutton.png')
        self.button = pygame.transform.scale_by(self.button, 2)
        self.boxx = 0
        self.boxy = 0
        self.music = False
        self.fade = (0, 0, 0, 200)
        self.dialogue = Dialogue()
        
    def update(self, playerrect, tomatorect, markrect, furretrect, speaking, displayInfo, walking, iterate, tomatolvl):
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
        self.boxx = int((self.dispw/2)-(self.box.get_width()/2))
        self.boxy = int((self.disph/10*9)-(self.box.get_height()))

        if pygame.Rect.colliderect(self.playerrect, self.tomatorect) and self.speaking:
            self.specnpc = "tomato"
            if self.music == False:
                pygame.mixer.music.fadeout(1000)
                if tomatolvl <= 1:
                    pygame.mixer.music.load('audio\\tomton.mp3')
                elif tomatolvl > 1:
                    pygame.mixer.music.load('audio\\tomtoneo.mp3')
                pygame.mixer.music.set_volume(0.2)
                pygame.mixer.music.play(-1)
                self.music = True
            if tomatolvl < 1:
                self.npc = pygame.image.load('images\\tomato\\tomat.png')
                self.npcx = int((self.dispw/2)-(self.npc.get_width()/2)) 
                self.npcy = int((self.disph/2-(self.disph/10))-(self.npc.get_height()/2))
            elif tomatolvl == 1:
                self.npc = pygame.image.load('images\\tomato\\tomto.png')
                self.npcx = int((self.dispw/2)-(self.npc.get_width()/2)) 
                self.npcy = int((self.disph/2-(self.disph/10))-(self.npc.get_height()/2))
            else:
                self.npc = pygame.image.load('images\\tomato\\tomtonneo.png')
                self.npc = pygame.transform.scale(self.npc, (self.npc.get_width()/2.5, self.npc.get_height()/2.5))
                self.npcx = int((self.dispw/2)-(self.npc.get_width()/2)) 
                self.npcy = int((self.disph/2-(self.disph/10*5))-(self.npc.get_height()/2))
        
        elif pygame.Rect.colliderect(self.playerrect, self.markrect) and self.speaking:
            self.specnpc = "mark"
            self.npc = pygame.image.load('images\\markiplier\\mark.png')
            self.npcx = int((self.dispw/2)-(self.npc.get_width()/2)) 
            self.npcy = int((self.disph/2-(self.disph/10))-(self.npc.get_height()/2))
        
        elif pygame.Rect.colliderect(self.playerrect, self.furretrect) and self.speaking:
            self.specnpc = "furret"
            if self.music == False:
                pygame.mixer.music.fadeout(1000)
                pygame.mixer.music.load('audio\\walk.mp3')
                pygame.mixer.music.set_volume(0.2)
                pygame.mixer.music.play(-1)
                self.music = True
            if walking <= 12: 
                self.npc = pygame.image.load('images\\furret\\furret1.png')
            else:
                self.npc = pygame.image.load('images\\furret\\furret2.png')
            self.npcx = int((self.dispw/2)-(self.npc.get_width()/2)) 
            self.npcy = int((self.disph/2-(self.disph/10))-(self.npc.get_height()/2))

    def draw(self, surface):
        if ((pygame.Rect.colliderect(self.playerrect, self.tomatorect) and self.speaking) or (pygame.Rect.colliderect(self.playerrect, self.markrect) 
             and self.speaking) or (pygame.Rect.colliderect(self.playerrect, self.furretrect) and self.speaking)):
            pygame.draw.rect(self.bgsurf, self.fade, self.bgsurf.get_rect())
            surface.blit(self.bgsurf, (0, 0))
            surface.blit(self.npc, (self.npcx, self.npcy))
            surface.blit(self.box, (self.boxx, self.boxy))
            surface.blit(self.button, (1696, 798))
            if self.iterate == True:
                self.dialogue.update(self.speaking, self.specnpc)
            self.dialogue.draw(surface)

class Prompt():
    def __init__(self, identity):
        self.prompt = pygame.image.load('images\\dialogue\\eprompt.png')
        self.x = identity.x + (identity.character.get_width() / 2) - (self.prompt.get_width() / 2)
        self.y = identity.y - self.prompt.get_height() - 8
        self.beendone1 = False
        self.beendone2 = False

    def update(self, wdown, adown, sdown, ddown, speaking, id="", tomatolvl = 0):
        self.x, self.y = upd_pos(self.x, self.y, wdown, adown, sdown, ddown)
        self.speaking = speaking

        if id == "tomato":
            if tomatolvl == 1 and not self.beendone1:
                self.y -= 96
                self.beendone1 = True
            elif tomatolvl > 1 and not self.beendone2:
                self.y -= 250
                self.beendone2 = True

    def draw(self, surface, playerrect, npcrect):
        if pygame.Rect.colliderect(playerrect, npcrect) and not self.speaking:
            surface.blit(self.prompt, (self.x, self.y))

class NPC():
    def __init__(self, character, identity, x, y):
        self.character = pygame.transform.scale(character, (character.get_width()/2.5, character.get_height()/2.5))
        self.identifier = identity
        self.x = x
        self.y = y
        self.beendone1 = False
        self.beendone2 = False

    def update(self, wdown, adown, sdown, ddown, id="", tomatolvl=0):
        self.x, self.y = upd_pos(self.x, self.y, wdown, adown, sdown, ddown)
        
        if id == "tomato":
            if tomatolvl == 1 and not self.beendone1:
                self.tomto = pygame.image.load('images\\tomato\\tomto.png')
                self.tomto = pygame.transform.scale(self.tomto, (self.tomto.get_width()/2.5, self.tomto.get_height()/2.5))
                self.x -= self.tomto.get_width()//2 - self.character.get_width()//2 + 2
                self.y -= self.tomto.get_height() - self.character.get_height() - 16
                self.character = self.tomto
                self.beendone1 = True
            elif tomatolvl > 1 and not self.beendone2:
                self.tomtonneo = pygame.image.load('images\\tomato\\tomtonneo.png')
                self.tomtonneo = pygame.transform.scale(self.tomtonneo, (self.tomtonneo.get_width()/4, self.tomtonneo.get_height()/4))
                self.x -= self.tomtonneo.get_width()//2 - self.character.get_width()//2 + 20
                self.y -= self.tomtonneo.get_height()//10*8 + 10
                self.character = self.tomtonneo
                self.beendone2 = True
            
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
        self.x, self.y = upd_pos(self.x, self.y, wdown, adown, sdown, ddown)

    def draw(self, surface):
        surface.blit(self.sea, (self.x, self.y))

class Houseroof():
    def __init__(self, roof, x, y):
        self.roof = pygame.transform.scale(roof, (roof.get_width()/2.5, roof.get_height()/2.5))
        self.x = x
        self.y = y

    def update(self, wdown, adown, sdown, ddown): 
        self.x, self.y = upd_pos(self.x, self.y, wdown, adown, sdown, ddown)

    def draw(self, surface):
        surface.blit(self.roof, (self.x, self.y))

class Obstructable():
    def __init__(self, base, x, y):
        self.base = pygame.transform.scale(base, (base.get_width()/2.5, base.get_height()/2.5))
        self.x = x
        self.y = y
    
    def update(self, wdown, adown, sdown, ddown):
        self.x, self.y = upd_pos(self.x, self.y, wdown, adown, sdown, ddown)

    def draw(self, surface):
        surface.blit(self.base, (self.x, self.y))

class Paths():
    def __init__(self):
        self.background = pygame.image.load('images\\village\\pathsgrass.png')
        self.background = pygame.transform.scale(self.background, (self.background.get_width()/2.5, self.background.get_height()/2.5))
        self.x = -407
        self.y = -1950

    def update(self, wdown, adown, sdown, ddown):
        self.x, self.y = upd_pos(self.x, self.y, wdown, adown, sdown, ddown)

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
    (playerx, playery, playerw, playerh, playerrect, tomatorectobj, markrectobj, furretrectobj, collisions) = rect_creation()
    iterate = False
    speaking = False
    lastkey = ""
    black = (0,0,0)
    walking = 0
    tomatolvl = 0
    armed = False
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
                    playery = 672
                    playerrect = pygame.Rect(playerx, playery, playerw, playerh)

                else:
                    screen = pygame.display.set_mode(res, pygame.RESIZABLE)
                    playery = 642
                    playerrect = pygame.Rect(playerx, playery, playerw, playerh)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:

                if dialogue.dialogue.tomtoitrt >= len(dialogue.dialogue.tomtodlg):
                    speaking = False
                    dialogue.dialogue.tomtoitrt -= 1
                    dialogue.music = False
                    start_music()

                elif dialogue.dialogue.markitrt >= len(dialogue.dialogue.markdlg):
                    speaking = False
                    dialogue.dialogue.markitrt -= 1

                elif dialogue.dialogue.furretitrt >= len(dialogue.dialogue.furretdlg):
                    speaking = False
                    dialogue.dialogue.furretitrt -= 1
                    dialogue.music = False
                    start_music()
                
                elif dialogue.dialogue.tomtodlg[dialogue.dialogue.tomtoitrt] == 0:
                    speaking = False
                    dialogue.dialogue.tomtoitrt += 1
                    dialogue.music = False
                    start_music()
                    armed = True

                elif dialogue.dialogue.markdlg[dialogue.dialogue.markitrt] == 0:
                    speaking = False
                    dialogue.dialogue.markitrt += 1
                    dialogue.music = False
                    start_music()
                      
                elif dialogue.dialogue.furretdlg[dialogue.dialogue.furretitrt] == 0:
                    speaking = False
                    dialogue.dialogue.furretitrt += 1
                    dialogue.music = False
                    start_music()

                elif pygame.Rect.colliderect(playerrect, tomatorect) or pygame.Rect.colliderect(playerrect, markrect) or pygame.Rect.colliderect(playerrect, furretrect):
                    iterate = True
                    speaking = True
                    if armed == True:
                        tomatolvl += 1
                        armed = False

        # Game Logic
        walking += 1
        if walking >= 25:
            walking = 0
        displayInfo = pygame.display.Info()
        wdown, adown, sdown, ddown, lastkey = get_keydown(lastkey, speaking)
        playerrect, tomatorect, markrect, furretrect, wdown, adown, sdown, ddown = upd_rects(wdown, adown, sdown, ddown, playerrect, tomatorectobj, markrectobj, 
                                                                                             furretrectobj, collisions, playerx, playery, playerw, playerh)
        upd_code(displayInfo, wdown, adown, sdown, ddown, iterate, lastkey, walking, spacesea, background, house1base, house2base, house3base, rail1, rail2, player, 
                 house1roof, house2roof, house3roof, tomato, markiplier, furret, deity, tomatoprompt, markprompt, furretprompt, playerrect, tomatorect, 
                     markrect, furretrect, dialogue, speaking, tomatolvl)
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

    print(rail1.base.get_width(), rail1.base.get_height())
    print(rail2.base.get_width(), rail2.base.get_height())
    print(markiplier.character.get_width(), markiplier.character.get_height())
    print(furret.character.get_width(), furret.character.get_height())
    print(tomato.character.get_width(), tomato.character.get_height())

    return (player, background, spacesea, house1base, house2base, house3base, house1roof, house2roof, house3roof, rail1, rail2, tomato, markiplier, 
            furret, deity, tomatoprompt, markprompt, furretprompt, dialogue)

def rect_creation():
    collisions = []
    playerx = 876
    playery = 642
    playerw = 168
    playerh = 21
    playerrectcollis = pygame.Rect(playerx, playery, playerw, playerh)
    tomatorect = Rectangle(-399, -598, 533, 513)
    markrect = Rectangle(2145, -1346, 128, 288)
    furretrect = Rectangle(2301, -1012, 330, 142)

    house1collis = Rectangle(-15, -158, 744, 672)
    collisions.insert(0, house1collis)
    house2collis = Rectangle(1185, -158, 744, 672)
    collisions.insert(0, house2collis)
    house3collis = Rectangle(2033, -150, 744, 672)
    collisions.insert(0, house3collis)
    rail1collis = Rectangle(-399, -526, 2512, 104)
    collisions.insert(0, rail1collis)
    rail2collis = Rectangle(2305, -526, 720, 104)
    collisions.insert(0, rail2collis)
    tomatocollis = Rectangle(-199, -398, 133, 113)
    collisions.insert(0, tomatocollis)
    markcollis = Rectangle(2145, -1446, 128, 208)
    collisions.insert(0, markcollis)
    furretcollis = Rectangle(2401, -1062, 230, 152)
    collisions.insert(0, furretcollis)
    leftwall = Rectangle(-219, -423, 20, 1573)
    collisions.insert(0, leftwall)
    bottomwall = Rectangle(-219, 1130, 3064, 20)
    collisions.insert(0, bottomwall)
    rightwall = Rectangle(2825, -423, 20, 1573)
    collisions.insert(0, rightwall)
    dock1 = Rectangle(1849, -870, 264, 345)
    collisions.insert(0, dock1)
    dock2 = Rectangle(2305, -870, 264, 345)
    collisions.insert(0, dock2)
    dock3 = Rectangle(1829, -1070, 20, 250)
    collisions.insert(0, dock3)
    dock4 = Rectangle(2569, -1070, 20, 250)
    collisions.insert(0, dock4)
    dock5 = Rectangle(1849, -1286, 264, 264)
    collisions.insert(0, dock5)
    dock6 = Rectangle(2305, -1286, 264, 264)
    collisions.insert(0, dock6)
    dock7 = Rectangle(2084, -1306, 250, 20)
    collisions.insert(0, dock7)

    return playerx, playery, playerw, playerh, playerrectcollis, tomatorect, markrect, furretrect, collisions

def upd_code(displayInfo, wdown, adown, sdown, ddown, iterate, lastkey, walking, spacesea, background, house1base, house2base, house3base, rail1, rail2, player, house1roof, 
             house2roof, house3roof, tomato, markiplier, furret, deity, tomatoprompt, markprompt, furretprompt, playerrectcollis, tomatorect, markrect, furretrect, 
             dialogue, speaking, tomatolvl):
    spacesea.update(wdown, adown, sdown, ddown)
    background.update(wdown, adown, sdown, ddown)
    house1base.update(wdown, adown, sdown, ddown)
    house2base.update(wdown, adown, sdown, ddown)
    house3base.update(wdown, adown, sdown, ddown)
    rail1.update(wdown, adown, sdown, ddown)
    rail2.update(wdown, adown, sdown, ddown)
    tomato.update(wdown, adown, sdown, ddown, "tomato", tomatolvl)
    markiplier.update(wdown, adown, sdown, ddown)
    furret.update(wdown, adown, sdown, ddown)
    deity.update(wdown, adown, sdown, ddown)
    player.update(wdown, adown, sdown, ddown, lastkey, walking)
    house1roof.update(wdown, adown, sdown, ddown)
    house2roof.update(wdown, adown, sdown, ddown)
    house3roof.update(wdown, adown, sdown, ddown)
    tomatoprompt.update(wdown, adown, sdown, ddown, speaking, "tomato", tomatolvl)
    markprompt.update(wdown, adown, sdown, ddown, speaking)
    furretprompt.update(wdown, adown, sdown, ddown, speaking)
    dialogue.update(playerrectcollis, tomatorect, markrect, furretrect, speaking, displayInfo, walking, iterate, tomatolvl)

def upd_pos(x, y, wdown, adown, sdown, ddown):
    if wdown:
        y += 16
    if adown:
        x += 16
    if sdown:
        y -= 16
    if ddown:
        x -= 16
    if sdown and wdown:
        pass
    elif ddown and adown: 
        pass
    else:
        if wdown and adown:
            y -= 4
            x -= 4
        if wdown and ddown:
            y -= 4
            x += 4
        if sdown and adown:
            y += 4
            x -= 4
        if sdown and ddown:
            y += 4
            x += 4
        
    return x, y

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

def upd_rects(wdown, adown, sdown, ddown, playerrectcollis, tomatorect, markrect, furretrect, collisions, playerx, playery, playerw, playerh):
    colliding = False

    tomatorect.update(wdown, adown, sdown, ddown, colliding)
    markrect.update(wdown, adown, sdown, ddown, colliding)
    furretrect.update(wdown, adown, sdown, ddown, colliding)
    
    for object in collisions:
        object.update(wdown, adown, sdown, ddown, colliding)

    colliding, wdown, adown, sdown, ddown, skipy, skipx = checkcollis(playerrectcollis, collisions, wdown, adown, sdown, ddown, playerx, playery, playerw, playerh)

    if colliding:
        tomatorect.update(wdown, adown, sdown, ddown, colliding, skipy, skipx)
        markrect.update(wdown, adown, sdown, ddown, colliding, skipy, skipx)
        furretrect.update(wdown, adown, sdown, ddown, colliding, skipy, skipx)
        for object in collisions:
            object.update(wdown, adown, sdown, ddown, colliding, skipy, skipx)

    return playerrectcollis, tomatorect.rectangle, markrect.rectangle, furretrect.rectangle, wdown, adown, sdown, ddown

def checkcollis(playerrectcollis, collisions, wdown, adown, sdown, ddown, playerx, playery, playerw, playerh):
    colliding = False
    skipy = False
    skipx = False
    for obstructable in collisions:
        if pygame.Rect.colliderect(playerrectcollis, obstructable.rectangle):
            colliding = True
            if wdown and ((playerx < obstructable.x + obstructable.width) or (playerx+playerw > obstructable.x)) and (playery+playerh > obstructable.y + obstructable.height):
                wdown = False
                skipy = True
            if adown and ((playery < obstructable.y + obstructable.height) or (playery+playerh > obstructable.y)) and (playerx+playerw > obstructable.x + obstructable.width):
                adown = False
                skipx = True
            if sdown and ((playerx < obstructable.x + obstructable.width) or (playerx+playerw > obstructable.x)) and (playery < obstructable.y):
                sdown = False
                skipy = True
            if ddown and ((playery < obstructable.y + obstructable.height) or (playery+playerh > obstructable.y)) and (playerx < obstructable.x):
                ddown = False
                skipx = True

    return colliding, wdown, adown, sdown, ddown, skipy, skipx

def start_music():
    if pygame.mixer.music.get_busy:
        pygame.mixer.music.fadeout(1000)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.load('audio\\astoryabouttheendoftheworld.mp3')
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.load('audio\\astoryabouttheendoftheworld.mp3')
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

if __name__ == "__main__":
    main()