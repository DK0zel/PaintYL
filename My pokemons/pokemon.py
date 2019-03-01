import os
import pygame

size = width, height = 1280, 720
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Pokemon')

rttt = False

FPS = 60
clock = pygame.time.Clock()

StartScreen = pygame.image.load('Start.png')
StartScreen.set_colorkey((0,0,0))
screen.blit(StartScreen,(0,0))

charizard = pygame.image.load('Charizard.png')
venusaur = pygame.image.load('Venusaur.png')
starmie = pygame.image.load('Starmie.png')


Watergun = [70,'water']
FireBlust = [70, 'fire']
Tackle = [40,'normal']
Psychic = [60, 'psychic']
ShadowBall = [70, 'ghost']
GrassKnot = [70, 'grass']
IceSpear = [50, 'ice']
Gigadrain = [60,'grass']
Flamethrower = [100, 'fire']
HydroPump = [100, 'water']

Charizard = [297,267,228,328,'fire',Tackle,FireBlust,Flamethrower,(410,385),charizard,'Charizard']
Venusaur = [301,299,299,196,'grass',Tackle,GrassKnot,Gigadrain,(410,410),venusaur,'Venusaur']
Blastoise = [299,269,309,193,'water',Tackle,Watergun,HydroPump]
Starmie = [261,299,206,361,'psychic',Tackle,Watergun, Psychic,(420,410),starmie,'Starmie']
Gengar = [261,359,186,350,'ghost',Tackle,ShadowBall,Gigadrain]
Cloyster = [241,290,350,177,'ice',Tackle,Watergun,IceSpear]

AllPokemon = [Charizard,Venusaur,Blastoise,Starmie,Gengar,Cloyster]
playerP = [Charizard, Venusaur, Starmie]
botP = [Blastoise,Gengar,Cloyster]

pygame.display.update()

do = True
WHITE = (255, 255, 255)
multi = 1
print('Press Space')
green = (0,0,0)
while do:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            do = False
        elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_SPACE:
                        screen.fill(WHITE)
                        fm = pygame.image.load('First message.png')
                        screen.blit(fm,(700,150))                        
                        screen.blit(charizard,(200,270))
                        screen.blit(venusaur,(400,270))
                        screen.blit(starmie,(600,270))
                        fs1 = pygame.image.load('1fs.png')
                        screen.blit(fs1,(215,370))
                        fs2 = pygame.image.load('2fs.png')
                        screen.blit(fs2,(400,370))
                        fs3 = pygame.image.load('3fs.png')
                        screen.blit(fs3,(600,370))                        
                        do = False
    pygame.display.update()     
    clock.tick(FPS)
    
    
do = True

pokeball = pygame.image.load('pokeball.png')
arena = pygame.image.load('arena.png')

gengar = pygame.image.load('Gengar.png')
blastoise = pygame.image.load('Blastoise.png')
cloyster = pygame.image.load('Cloyster.png')

watergun = pygame.image.load('Water2.png')
fireBlust = pygame.image.load('fire2.png')
tackle = pygame.image.load('takle.png')
psychic = pygame.image.load('Psychic.png')
shadowBall = pygame.image.load('Ghost.png')
grassKnot = pygame.image.load('Grass1.png')
iceSpear = pygame.image.load('Ice.png')
gigadrain = pygame.image.load('Grass2.png')
flamethrower = pygame.image.load('Fire1.png')
hydroPump = pygame.image.load('Water1.png')

nextp = pygame.image.load('next.png')

nowbot = Gengar

while do:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            do = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_1:
                screen.blit(arena,(0,0))
                screen.blit(charizard,(410,385))
                screen.blit(pokeball,(50,680))
                screen.blit(pokeball,(80,680))
                screen.blit(pokeball,(1240,15))
                screen.blit(pokeball,(1210,15))
                screen.blit(gengar,(785,405))
                nowplayer = Charizard
                do = False
            elif e.key == pygame.K_2:
                screen.blit(arena,(0,0))
                screen.blit(venusaur,(410,410))
                screen.blit(pokeball,(50,680))
                screen.blit(pokeball,(80,680))
                screen.blit(pokeball,(1240,15))
                screen.blit(pokeball,(1210,15))
                screen.blit(gengar,(785,405))
                nowplayer = Venusaur
                do = False
            elif e.key == pygame.K_3:
                screen.blit(arena,(0,0)) 
                screen.blit(starmie,(420,410))
                screen.blit(pokeball,(50,680))
                screen.blit(pokeball,(80,680))
                screen.blit(pokeball,(1240,15))
                screen.blit(pokeball,(1210,15))
                screen.blit(gengar,(785,405))
                nowplayer = Starmie
                do = False
    pygame.display.update()     
    clock.tick(FPS)     
k = 1
do = True
bt = 3
pt = 3
while do:
    if k == 1:
        if nowplayer == Charizard:
            screen.blit(tackle,(190,670))
            screen.blit(fireBlust,(390,670))
            screen.blit(flamethrower,(590,670))          
        elif nowplayer == Venusaur:
            screen.blit(tackle,(190,670))
            screen.blit(grassKnot,(390,670))
            screen.blit(gigadrain,(590,670))            
        elif nowplayer == Starmie:
            screen.blit(tackle,(190,670))
            screen.blit(psychic,(390,670))
            screen.blit(watergun,(590,670))            
        pygame.display.update()  
        k = 0
    pygame.display.update() 
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            do = False
        elif e.type == pygame.KEYDOWN:
            if nowplayer == Charizard:
                if(nowplayer[3]>nowbot[3]):
                    if e.key == pygame.K_1:
                        nowbot[0] += nowbot[2] - (nowplayer[1]*1.2)
                        if(nowbot[0]>0):
                            nowplayer[0] += nowplayer[2] - (nowbot[1]*1.3)
                        a,b = str(nowplayer[0]),str(nowbot[0])
                        c = a + ',' + b
                        print(c)    
                    elif e.key == pygame.K_2:
                        nowbot[0] += nowbot[2] - (nowplayer[1]*1.5)
                        if(nowbot[0]>0):
                            nowplayer[0] += nowplayer[2] - (nowbot[1]*1.3)
                        a,b = str(nowplayer[0]),str(nowbot[0])
                        c = a + ',' + b
                        print(c)                             
                    elif e.key == pygame.K_3:
                        nowbot[0] += nowbot[2] - (nowplayer[1]*1.5)
                        if(nowbot[0]>0):
                            nowplayer[0] += nowplayer[2] - (nowbot[1]*1.3)
                        a,b = str(nowplayer[0]),str(nowbot[0])
                        c = a + ',' + b
                        print(c)                          
                else:
                    if e.key == pygame.K_1:
                        nowplayer[0] += nowplayer[2] - (nowbot[1]*1.3)
                        if(nowplayer[0]>0):
                            nowbot[0] += nowbot[2] - (nowplayer[1]*1.2)
                        a,b = str(nowplayer[0]),str(nowbot[0])
                        c = a + ',' + b
                        print(c)     
                    elif e.key == pygame.K_2:
                        nowplayer[0] += nowplayer[2] - (nowbot[1]*1.3)
                        if(nowplayer[0]>0):
                            nowbot[0] += nowbot[2] - (nowplayer[1]*1.5)
                        a,b = str(nowplayer[0]),str(nowbot[0])
                        c = a + ',' + b
                        print(c)                           
                    elif e.key == pygame.K_3:
                        nowplayer[0] += nowplayer[2] - (nowbot[1]*1.3)
                        if(nowplayer[0]>0):
                            nowbot[0] += nowbot[2] - (nowplayer[1]*1.5)
                        a,b = str(nowplayer[0]),str(nowbot[0])
                        c = a + ',' + b
                        print(c)   
            elif nowplayer == Venusaur:                 
                if(nowplayer[3]>nowbot[3]):
                    if e.key == pygame.K_1:
                        nowbot[0] += nowbot[2] - (nowplayer[1]*1.2)
                        if(nowbot[0]>0):
                            nowplayer[0] += nowplayer[2] - (nowbot[1]*1.3)
                        a,b = str(nowplayer[0]),str(nowbot[0])
                        c = a + ',' + b
                        print(c)    
                    elif e.key == pygame.K_2:
                        nowbot[0] += nowbot[2] - (nowplayer[1]*1.5)
                        if(nowbot[0]>0):
                            nowplayer[0] += nowplayer[2] - (nowbot[1]*1.3)
                        a,b = str(nowplayer[0]),str(nowbot[0])
                        c = a + ',' + b
                        print(c)                             
                    elif e.key == pygame.K_3:
                        nowbot[0] += nowbot[2] - (nowplayer[1]*1.5)
                        nowplayer[0] += (nowbot[2] - (nowplayer[1]*1.5))/2
                        if(nowbot[0]>0):
                            nowplayer[0] += nowplayer[2] - (nowbot[1]*1.3)
                        a,b = str(nowplayer[0]),str(nowbot[0])
                        c = a + ',' + b
                        print(c)               
                else:
                    if e.key == pygame.K_1:
                        nowplayer[0] += nowplayer[2] - (nowbot[1]*1.3)
                        if(nowplayer[0]>0):
                            nowbot[0] += nowbot[2] - (nowplayer[1]*1.2)
                        a,b = str(nowplayer[0]),str(nowbot[0])
                        c = a + ',' + b
                        print(c)     
                    elif e.key == pygame.K_2:
                        nowplayer[0] += nowplayer[2] - (nowbot[1]*1.3)
                        if(nowplayer[0]>0):
                            nowbot[0] += nowbot[2] - (nowplayer[1]*1.5)
                        a,b = str(nowplayer[0]),str(nowbot[0])
                        c = a + ',' + b
                        print(c)                           
                    elif e.key == pygame.K_3:
                        nowplayer[0] += nowplayer[2] - (nowbot[1]*1.3)
                        if(nowplayer[0]>0):
                            nowbot[0] += nowbot[2] - (nowplayer[1]*1.5)
                        a,b = str(nowplayer[0]),str(nowbot[0])
                        c = a + ',' + b
                        print(c)   
                        print(a)             
            elif nowplayer == Starmie:                  
                if(nowplayer[3]>nowbot[3]):
                    if e.key == pygame.K_1:
                        nowbot[0] += nowbot[2] - (nowplayer[1]*1.2)
                        if(nowbot[0]>0):
                            nowplayer[0] += nowplayer[2] - (nowbot[1]*1.3)
                        a,b = str(nowplayer[0]),str(nowbot[0])
                        c = a + ',' + b
                        print(c)    
                    elif e.key == pygame.K_2:
                        nowbot[0] += nowbot[2] - (nowplayer[1]*1.5)
                        if(nowbot[0]>0):
                            nowplayer[0] += nowplayer[2] - (nowbot[1]*1.3)
                        a,b = str(nowplayer[0]),str(nowbot[0])
                        c = a + ',' + b
                        print(c)                             
                    elif e.key == pygame.K_3:
                        nowbot[0] += nowbot[2] - (nowplayer[1]*1.5)
                        if(nowbot[0]>0):
                            nowplayer[0] += nowplayer[2] - (nowbot[1]*1.3)
                        a,b = str(nowplayer[0]),str(nowbot[0])
                        c = a + ',' + b
                        print(c)               
                else:
                    if e.key == pygame.K_1:
                        nowplayer[0] += nowplayer[2] - (nowbot[1]*1.3)
                        if(nowplayer[0]>0):
                            nowbot[0] += nowbot[2] - (nowplayer[1]*1.2)
                        a,b = str(nowplayer[0]),str(nowbot[0])
                        c = a + ',' + b
                        print(c)     
                    elif e.key == pygame.K_2:
                        nowplayer[0] += nowplayer[2] - (nowbot[1]*1.3)
                        if(nowplayer[0]>0):
                            nowbot[0] += nowbot[2] - (nowplayer[1]*1.5)
                        a,b = str(nowplayer[0]),str(nowbot[0])
                        c = a + ',' + b
                        print(c)                           
                    elif e.key == pygame.K_3:
                        nowplayer[0] += nowplayer[2] - (nowbot[1]*1.3)
                        if(nowplayer[0]>0):
                            nowbot[0] += nowbot[2] - (nowplayer[1]*1.5)
                        a,b = str(nowplayer[0]),str(nowbot[0])
                        c = a + ',' + b
                        print(c)
    pygame.display.update()     
    clock.tick(FPS)    
    if(nowbot[0] <= 0 and bt == 3):
        screen.fill(WHITE)
        screen.blit(arena,(0,0))
        print('Gengar faint')
        bt -= 1
        nowbot = Cloyster
        screen.blit(cloyster,(800,410))
        screen.blit(pokeball,(1240,15))
        if(nowplayer == Venusaur):
            screen.blit(tackle,(190,670))
            screen.blit(grassKnot,(390,670))
            screen.blit(gigadrain,(590,670))                        
            if(pt == 3):
                screen.blit(pokeball,(50,680))
                screen.blit(pokeball,(80,680))
                screen.blit(venusaur,(410,410))
                
            elif(pt == 2):
                screen.blit(pokeball,(50,680)) 
                screen.blit(venusaur,(410,410))
            else:
                screen.blit(venusaur,(410,410))
        elif(nowplayer == Charizard):
            screen.blit(tackle,(190,670))
            screen.blit(fireBlust,(390,670))
            screen.blit(flamethrower,(590,670))                
            if(pt == 3):
                screen.blit(pokeball,(50,680))
                screen.blit(pokeball,(80,680))
                screen.blit(charizard,(410,410))
                
            elif(pt == 2):
                screen.blit(pokeball,(50,680)) 
                screen.blit(charizard,(410,410))
            else:
                screen.blit(charizard,(410,410))            
        elif(nowplayer == Starmie):
            screen.blit(tackle,(190,670))
            screen.blit(psychic,(390,670))
            screen.blit(watergun,(590,670))                        
            if(pt == 3):
                screen.blit(pokeball,(50,680))
                screen.blit(pokeball,(80,680))
                screen.blit(starmie,(410,410))
                
            elif(pt == 2):
                screen.blit(pokeball,(50,680)) 
                screen.blit(starmie,(410,410))
            else:
                screen.blit(starmie,(410,410))            
    elif nowbot[0] <= 0 and bt == 2:
        print('Cloyster faint')
        bt -= 1
        screen.blit(arena,(0,0))
        nowbot = Blastoise
        screen.blit(blastoise,(800,410))
        if(nowplayer == Venusaur):
            screen.blit(tackle,(190,670))
            screen.blit(grassKnot,(390,670))
            screen.blit(gigadrain,(590,670))                        
            if(pt == 3):
                screen.blit(pokeball,(50,680))
                screen.blit(pokeball,(80,680))
                screen.blit(venusaur,(410,410))
                
            elif(pt == 2):
                screen.blit(pokeball,(50,680)) 
                screen.blit(venusaur,(410,410))
            else:
                screen.blit(venusaur,(410,410))
        elif(nowplayer == Charizard):
            screen.blit(tackle,(190,670))
            screen.blit(fireBlust,(390,670))
            screen.blit(flamethrower,(590,670))                
            if(pt == 3):
                screen.blit(pokeball,(50,680))
                screen.blit(pokeball,(80,680))
                screen.blit(charizard,(410,410))
                
            elif(pt == 2):
                screen.blit(pokeball,(50,680)) 
                screen.blit(charizard,(410,410))
            else:
                screen.blit(charizard,(410,410))            
        elif(nowplayer == Starmie):
            screen.blit(tackle,(190,670))
            screen.blit(psychic,(390,670))
            screen.blit(watergun,(590,670))                        
            if(pt == 3):
                screen.blit(pokeball,(50,680))
                screen.blit(pokeball,(80,680))
                screen.blit(starmie,(410,410))
                
            elif(pt == 2):
                screen.blit(pokeball,(50,680)) 
                screen.blit(starmie,(410,410))
            else:
                screen.blit(starmie,(410,410))          
    elif nowbot[0] <= 0 and bt == 1:
        print('Blastoise faint')
        print('You win')
        win = pygame.image.load('win.jpg')
        screen.blit(win,(700,250))
        do = False
    elif(nowplayer[0] <= 0):
        k = 1
        r = str(nowplayer[-1])
        print(r + ' ' + 'faint')
        pt -= 1
        if rttt:
            print('You lose')
            lose = pygame.image.load('lose.jpg')
            screen.blit(lose,(0,0))
            pygame.display.update()        
        if(len(playerP) == 2):
            pt = 0
            rttt = True
            playerP.remove(nowplayer)
            screen.blit(arena,(0,0))
            if playerP[0][-1] == 'Charizard':
                nowplayer = Charizard
                mj = charizard
            elif playerP[0][-1] == 'Venusaur':
                nowplayer = Venusaur
                mj = venusaur
            elif playerP[0][-1] == 'Starmie':
                nowplayer = Starmie
                mj = starmie             
            if(bt == 3):
                screen.blit(pokeball,(1240,15))
                screen.blit(pokeball,(1210,15))
                screen.blit(gengar,(785,405))
                screen.blit(mj,(400,405))
            elif(bt == 2):
                screen.blit(pokeball,(1240,15))
                screen.blit(cloyster,(785,405))
                screen.blit(mj,(400,405))
            elif(bt == 1):
                screen.blit(blastoise,(800,410))
                screen.blit(mj,(400,405))
        elif rttt:
            print('You lose')
            lose = pygame.image.load('lose.jpg')
            screen.blit(lose,(700,250))
            pygame.display.update()
            do = False        
        elif pt > 0:
            screen.fill(WHITE)
            screen.blit(nextp,(490,70))
            playerP.remove(nowplayer)
            pygame.display.update()  
            ap = True
            if pt == 2:
                screen.blit(playerP[0][-2],(500,250))
                screen.blit(playerP[1][-2],(700,250))
                pygame.display.update()
                while ap:
                    for e in pygame.event.get():
                        if e.type == pygame.QUIT:
                            do = False
                            ap = False
                        elif e.type == pygame.KEYDOWN:
                            if e.key == pygame.K_1:
                                ap = False
                                screen.blit(arena,(0,0))
                                screen.blit(pokeball,(50,680))
                                if(bt == 3):
                                    screen.blit(pokeball,(1240,15))
                                    screen.blit(pokeball,(1210,15))
                                    screen.blit(gengar,(785,405))
                                    if playerP[0][-1] == 'Charizard':
                                        nowplayer = Charizard
                                        screen.blit(charizard,(410,385))
                                        pygame.display.update()
                                    elif playerP[0][-1] == 'Venusaur':
                                        nowplayer = Venusaur
                                        screen.blit(venusaur,(410,410))
                                        pygame.display.update()
                                    elif playerP[0][-1] == 'Starmie':
                                        nowplayer = Starmie
                                        screen.blit(starmie,(420,410))
                                        pygame.display.update()
                                elif(bt == 2):
                                    screen.blit(pokeball,(1210,15))
                                    screen.blit(cloyster,(785,405))
                                    if playerP[0][-1] == 'Charizard':
                                        nowplayer = Charizard
                                        screen.blit(charizard,(410,385))
                                        pygame.display.update()
                                    elif playerP[0][-1] == 'Venusaur':
                                        nowplayer = Venusaur
                                        screen.blit(venusaur,(410,410))
                                        pygame.display.update()
                                    elif playerP[0][-1] == 'Starmie':
                                        nowplayer = Starmie
                                        screen.blit(starmie,(420,410))
                                        pygame.display.update()
                                else:
                                    screen.blit(Blastoise,(785,405))
                                    if playerP[0][-1] == 'Charizard':
                                        nowplayer = Charizard
                                        screen.blit(charizard,(410,385))
                                        pygame.display.update()
                                    elif playerP[0][-1] == 'Venusaur':
                                        nowplayer = Venusaur
                                        screen.blit(venusaur,(410,410))
                                        pygame.display.update()
                                    elif playerP[0][-1] == 'Starmie':
                                        nowplayer = Starmie
                                        screen.blit(starmie,(420,410))
                                        pygame.display.update()
                            elif e.key == pygame.K_2:
                                ap = False
                                screen.blit(arena,(0,0))
                                screen.blit(pokeball,(50,680))
                                pygame.display.update()
                                if(bt == 3):
                                    screen.blit(pokeball,(1240,15))
                                    screen.blit(pokeball,(1210,15))
                                    screen.blit(gengar,(785,405))
                                    pygame.display.update()
                                    if playerP[1][-1] == 'Charizard':
                                        nowplayer = Charizard
                                        screen.blit(charizard,(410,385))
                                    elif playerP[1][-1] == 'Venusaur':
                                        nowplayer = Venusaur
                                        screen.blit(venusaur,(410,410))
                                        pygame.display.update()
                                    elif playerP[1][-1] == 'Starmie':
                                        nowplayer = Starmie
                                        screen.blit(starmie,(420,410))
                                        pygame.display.update()
                                elif(bt == 2):
                                    screen.blit(pokeball,(1210,15))
                                    screen.blit(cloyster,(785,405))
                                    pygame.display.update()
                                    if playerP[1][-1] == 'Charizard':
                                        nowplayer = Charizard
                                        screen.blit(charizard,(410,385))
                                        pygame.display.update()
                                    elif playerP[1][-1] == 'Venusaur':
                                        nowplayer = Venusaur
                                        screen.blit(venusaur,(410,410))
                                    elif playerP[1][-1] == 'Starmie':
                                        nowplayer = Starmie
                                        screen.blit(starmie,(420,410))
                                        pygame.display.update()
                                else:
                                    screen.blit(Blastoise,(785,405))
                                    if playerP[1][-1] == 'Charizard':
                                        nowplayer = Charizard
                                        screen.blit(charizard,(410,385))
                                        pygame.display.update()
                                    elif playerP[1][-1] == 'Venusaur':
                                        nowplayer = Venusaur
                                        screen.blit(venusaur,(410,410))
                                    elif playerP[1][-1] == 'Starmie':
                                        nowplayer = Starmie
                                        screen.blit(starmie,(420,410))
                                        pygame.display.update()  
pygame.quit()