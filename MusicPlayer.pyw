import pygame
import time
from os import listdir
from os import getlogin
import random

musics=listdir("C:/Users/"+getlogin()+"/Music")

pygame.init()
pygame.display.set_icon(pygame.image.load("A/play.png"))
w=pygame.display.set_mode((360,182))
pygame.display.set_caption("Music Player")
img1=pygame.transform.scale(pygame.image.load("A/prev.png"),(100,100))
img2=pygame.transform.scale(pygame.image.load("A/pause.png"),(100,100))
img3=pygame.transform.scale(pygame.image.load("A/play.png"),(100,100))
img4=pygame.transform.scale(pygame.image.load("A/next.png"),(100,100))
img5=pygame.transform.scale(pygame.image.load("A/shufOFF.png"),(32,32))
img6=pygame.transform.scale(pygame.image.load("A/shufON.png"),(32,32))
img7=pygame.transform.scale(pygame.image.load("A/sound.png"),(32,32))
g=True

f1=pygame.font.SysFont("Comic Sans MS",20)
player=True
r=0
rr=0
err=""
shuf=False
vol=150

channel=pygame.mixer.Channel(0)
try:
    csound=pygame.mixer.Sound("C:/Users/"+getlogin()+"/Music/"+musics[r])
    csound.set_volume((vol-94)/251)
    channel.play(csound)
except:
    #print("Failed to load music")
    exit()
while g:
    time.sleep(0.01)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            g=False
            csound.stop()
    
    w.fill((10,10,10))

    (mx , my) = pygame.mouse.get_pos()
    (m1,m2,m3)=pygame.mouse.get_pressed()
    m1r=m1
    if m1==1 and mm1==1:
        m1=0
    else:
        if m1==1:
            mm1=1
        else:
            mm1=0
    if m1==1:
        if my>47:
            if mx<120:
                if shuf:
                    r=random.randint(0,len(musics)-1)
                else:
                    r=r-1
                    if r>len(musics)-1:
                        r=0
                try:
                    csound=pygame.mixer.Sound("C:/Users/"+getlogin()+"/Music/"+musics[r])
                    csound.set_volume((vol-94)/251)
                    channel.play(csound)
                    player=True
                    err=""
                except:
                    #print("Failed to load music")
                    err="Failed to load music "
            elif mx>240:
                if shuf:
                    r=random.randint(0,len(musics)-1)
                else:
                    r=r+1
                    if r>len(musics)-1:
                        r=0
                try:
                    csound=pygame.mixer.Sound("C:/Users/"+getlogin()+"/Music/"+musics[r])
                    csound.set_volume((vol-94)/251)
                    channel.play(csound)
                    player=True
                    err=""
                except:
                    #print("Failed to load music")
                    err="Failed to load music "
            else:
                if player:
                    player=False
                    channel.pause()
                else:
                    player=True
                    channel.unpause()
        else:
            if mx<52:
                if shuf:
                    shuf=False
                else:
                    shuf=True
    if mx>52 and my<47 and m1r==1:
        vol=mx
        if vol<94:
            vol=94
        if vol>345:
            vol=345
        csound.set_volume((vol-94)/251)
    if not(channel.get_busy()):
        if shuf:
            r=random.randint(0,len(musics)-1)
        else:
            r=r+1
            if r>len(musics)-1:
                r=0
        try:
            csound=pygame.mixer.Sound("C:/Users/"+getlogin()+"/Music/"+musics[r])
            csound.set_volume((vol-94)/251)
            channel.play(csound)
            player=True
            err=""
        except:
            #print("Failed to load music")
            err="Failed to load music "
    w.blit(img1,(10,52))
    w.blit(img4,(250,52))
    pygame.draw.line(w,(200,200,200),(94,26),(345,26),5)
    pygame.draw.circle(w,(150,150,150),(vol,26),10)
    if shuf:
        w.blit(img6,(10,10))
    else:
        w.blit(img5,(10,10))
    if player:
        w.blit(img3,(130,52))
    else:
        w.blit(img2,(130,52))
    w.blit(img7,(52,10))
    frnd=f1.render("Now playing : "+err+musics[r],True,(200,200,200))
    w.blit(frnd,(360-rr%(frnd.get_width()+360),152))
    rr=rr+1

    pygame.display.flip()
pygame.quit()