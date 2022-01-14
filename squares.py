import pygame, random
from pygame import mixer
from test_functions import bubble_sort,list_reverse,collision

pygame.init()

#screen
screen=pygame.display.set_mode((1600,900))
w=1600
h=750

#music
mixer.init()
mixer.music.load("sounds/soundtrack.mp3")
mixer.music.set_volume(0.7)
mixer.music.play(-1)

#settings
pygame.display.set_caption("SQARES")
icon=pygame.image.load('pictures/logo.png')
pygame.display.set_icon(icon)

#board
board=[ [ 0 for i in range(32) ] for j in range(15) ]
board[0][0]=1

#logo
l=pygame.image.load('pictures/logo.png')
l=pygame.transform.scale(l, (490, 100))

#font
font=pygame.font.Font('freesansbold.ttf', 35)
bigfont=pygame.font.Font('freesansbold.ttf', 45)

#timer
clock=pygame.time.Clock()
time=0.0
def timer(time):
    timer=font.render(str(time)+" sec",True,(255,255,255))
    screen.blit(timer, (10, 10))

#enter nickname
user_nick='Player'
color_p=(200,200,200)
color_a=(255,0,0)
color=color_p
active=False

#score
score=0
def scoreboard(score):
    scoreboard=font.render("Score: "+str(score),True,(255,255,255))
    screen.blit(scoreboard, (10,110))

#lives
lives=3
def flives(lives):
    livesgui=font.render("Lives: "+str(lives),True,(255,255,255))
    screen.blit(livesgui, (10,60))

#player
playerIMG=pygame.image.load('pictures/b.png')
playerIMG=pygame.transform.scale(playerIMG, (50, 50))
playerX=0
playerY=150
pX=playerX//50
pY=playerY//50-3
pXY=(pX,pY)
wp=playerIMG.get_width()
hp=playerIMG.get_height()
movement=50

def player(x,y):
    screen.blit(playerIMG, (x, y))

#object1
object1IMG=[]
object1X=[]
object1Y=[]

def object1(x,y,i):
    screen.blit(object1IMG[i], (x,y))

#object2
object2IMG=[]
object2X=[]
object2Y=[]

def object2(x,y,i):
    screen.blit(object2IMG[i], (x,y))

#heart
heartIMG=[]
heartX=[]
heartY=[]

def heart(x,y,i):
    screen.blit(heartIMG[i], (x,y))

#status of pressed key
up=False
down=False
left=False
right=False

#random available coordinates
def rngcord():
    if board!=[ [ 1 for i in range(32) ] for j in range(15) ]:
        while True:
            rngy=random.randint(0,14)
            rngx=random.randint(0,31)
            flag=False
            for i in board[rngy]:
                if i == 0:
                    flag=True
                    break
            if flag==True:
                while True:
                    if board[rngy][rngx]==0:
                        return rngx, rngy
                    else:
                        rngx=random.randint(0,31)
    
view=0
running=True

#main loop
while running:
    #background and logo
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (64,64,64), pygame.Rect(0, 150, 1600, 750))
    screen.blit(l, (555, 25))
    
    #main menu view
    if view==0:
        input_nick=pygame.Rect(555, 250, 490, 100)
        pygame.draw.rect(screen, color,input_nick ,2)
        
        playr=pygame.Rect(583, 650, 434, 85)
        pygame.draw.rect(screen,(0,0,0),playr)

        lbr=pygame.Rect(582, 500, 434, 85)
        pygame.draw.rect(screen, (0,0,0),lbr)

        lead=bigfont.render("LEADERBOARD",True,(255,0,0))
        screen.blit(lead, (620, 525))

        enickname=font.render("Enter your nickname:",True,(255,255,255))
        screen.blit(enickname, (555, 200))

        nickname=font.render(user_nick,True,color)
        screen.blit(nickname, (input_nick.x+20, input_nick.y+35))

        start=bigfont.render("PLAY",True,(0,255,0))
        screen.blit(start, (730, 675))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_nick.collidepoint(event.pos):
                    active=True
                    color=color_a
                elif lbr.collidepoint(event.pos):
                    view=3
                elif playr.collidepoint(event.pos):
                    view=1
                    timestart=pygame.time.get_ticks()
                else:
                    active=False
                    color=color_p

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running=False
                else:
                    if active==True:
                        if event.key == pygame.K_BACKSPACE:
                            user_nick = user_nick[:-1]
                        else:
                            if len(user_nick)<20:
                                user_nick += event.unicode

    #game view            
    elif view==1:
        player(playerX, playerY)

        time=round((pygame.time.get_ticks()-timestart)/1000.0, 2)
        clocktime=round(time,1)
        
        nickname=font.render(user_nick,True,(255,255,255))
        screen.blit(nickname, (1200, 45))

        tupleXY=font.render(str(pXY),True,(255,255,255))
        screen.blit(tupleXY, (1200,85))

        timer(clocktime)
        scoreboard(score)
        flives(lives)

        #game over if
        if lives<=0:
            firstline=False

            file=open("scores.txt","r")
            if len(file.readlines())!=0:
                firstline=True
            file.close()

            f=open("scores.txt","a")
            if firstline==False:
                string=user_nick+"\n"+str(score)+"\n"+str(time)
            else:
                string="\n"+user_nick+"\n"+str(score)+"\n"+str(time)
            f.write(string)
            f.close()
            gotime=time
            goscore=score
            view=2
            lives=3
            score=0
            playerX=0
            playerY=150
            pX=playerX//50
            pY=playerY//50-3
            pXY=(pX,pY)
            object1IMG=[]
            object1X=[]
            object1Y=[]
            object2IMG=[]
            object2X=[]
            object2Y=[]
            heartIMG=[]
            heartX=[]
            heartY=[]
            board=[ [ 0 for i in range(32) ] for j in range(15) ]
            board[0][0]=1

        #red square
        if time%0.5==0 and board!=[ [ 1 for i in range(32) ] for j in range(15) ]:
            obj2=pygame.image.load('pictures/a.png')
            obj2=pygame.transform.scale(obj2, (50, 50))
            object2IMG.append(obj2)
            obj2x,obj2y=rngcord()
            board[obj2y][obj2x]=1
            object2X.append(obj2x*50)
            object2Y.append(obj2y*50+150)

        for i in range(len(object2IMG)):
            if collision(object2IMG,object2X,object2Y,i,playerIMG,playerX,playerY):
                lives-=1
                del object2IMG[i]
                del object2X[i]
                del object2Y[i]
                break
        
        for i in range(len(object2IMG)):
            object2(object2X[i], object2Y[i], i)
        
        #green square
        if time%0.5==0 and board!=[ [ 1 for i in range(32) ] for j in range(15) ]:
            obj1=pygame.image.load('pictures/c.png')
            obj1=pygame.transform.scale(obj1, (50, 50))
            object1IMG.append(obj1)
            obj1x,obj1y=rngcord()
            board[obj1y][obj1x]=1
            object1X.append(obj1x*50)
            object1Y.append(obj1y*50+150)

        for i in range(len(object1IMG)):
            if collision(object1IMG,object1X,object1Y,i,playerIMG,playerX,playerY):
                score+=1
                del object1IMG[i]
                del object1X[i]
                del object1Y[i]
                break

        for i in range(len(object1IMG)):
            object1(object1X[i], object1Y[i], i)
        
        #heart square
        if time%5==0 and board!=[ [ 1 for i in range(32) ] for j in range(15) ]:
            heartf=pygame.image.load('pictures/s.png')
            heartf=pygame.transform.scale(heartf, (50, 50))
            heartIMG.append(heartf)
            hx,hy=rngcord()
            board[hy][hx]=1
            heartX.append(hx*50)
            heartY.append(hy*50+150)

        for i in range(len(heartIMG)):
            if collision(heartIMG,heartX,heartY,i,playerIMG,playerX,playerY):
                lives+=1
                del heartIMG[i]
                del heartX[i]
                del heartY[i]
                break

        for i in range(len(heartIMG)):
            heart(heartX[i], heartY[i], i)
        
        #control
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and up==False:
                    up=True
                    board[pY][pX]=0
                    playerY-=movement
                    pXY=(pX,pY)
                    if playerY>=150:
                        pY=playerY//50-3
                        board[pY][pX]=1
                        pXY=(pX,pY)
                if event.key == pygame.K_DOWN and down==False:
                    down=True
                    board[pY][pX]=0
                    playerY+=movement
                    pXY=(pX,pY)
                    if playerY<900:
                        pY=playerY//50-3
                        board[pY][pX]=1
                        pXY=(pX,pY)
                if event.key == pygame.K_LEFT and left==False:
                    left=True
                    board[pY][pX]=0
                    playerX-=movement
                    pXY=(pX,pY)
                    if playerX>=0:
                        pX=playerX//50
                        board[pY][pX]=1
                        pXY=(pX,pY)
                if event.key == pygame.K_RIGHT and right==False:
                    right=True
                    board[pY][pX]=0
                    playerX+=movement
                    pXY=(pX,pY)
                    if playerX<1600:
                        pX=playerX//50
                        board[pY][pX]=1
                        pXY=(pX,pY)
                if event.key == pygame.K_ESCAPE:
                    running=False
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    up=False
                if event.key == pygame.K_DOWN:
                    down=False
                if event.key == pygame.K_LEFT:
                    left=False
                if event.key == pygame.K_RIGHT:
                    right=False
                
        #wrapping
        if playerX<0:
            playerX=w-wp
            pX=playerX//50
            board[pY][pX]=1
            pXY=(pX,pY)
        if playerX>w-wp:
            playerX=0
            pX=playerX//50
            board[pY][pX]=1
            pXY=(pX,pY)
        if playerY<150:
            playerY=900-hp
            pY=playerY//50-3
            board[pY][pX]=1
            pXY=(pX,pY)
        if playerY>900-hp:
            playerY=150
            pY=playerY//50-3
            board[pY][pX]=1
            pXY=(pX,pY)

        clock.tick(60)

    #game over view
    elif view==2:
        menur=pygame.Rect(583, 500, 434, 85)
        pygame.draw.rect(screen,(0,0,0),menur)

        gameover=bigfont.render("GAME OVER!",True,(255,0,0))
        screen.blit(gameover, (652, 200))

        nicktext=font.render(user_nick,True,(255,255,255))
        screen.blit(nicktext, (652, 300))

        timetext=font.render("Time: "+str(gotime)+" sec",True,(255,255,255))
        screen.blit(timetext, (652, 350))

        scoretext=font.render("Score: "+str(goscore)+" points",True,(255,255,255))
        screen.blit(scoretext, (652, 400))

        backtext=font.render("BACK TO MENU",True,(0,255,0))
        screen.blit(backtext, (menur.x+80, menur.y+28))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menur.collidepoint(event.pos):
                    view=0
    #leaderboard
    elif view==3:
        bmenur=pygame.Rect(583, 775, 434, 85)
        pygame.draw.rect(screen,(0,0,0),bmenur)    

        backmtext=font.render("BACK TO MENU",True,(0,255,0))
        screen.blit(backmtext, (bmenur.x+80, bmenur.y+28))     

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bmenur.collidepoint(event.pos):
                    view=0

        fr = open("scores.txt","r")
        leaderboarddict=[]
        leaderboardrecord=[]
        content=fr.readlines()
        length=len(content)
        for i in range(length):
            content[i]=content[i].replace("\n","")
        for i in range(0,length,3):
            leaderboarddict.append({"nick":content[i],"score":int(content[i+1]),"time":content[i+2]})

        #bubblesort
        leaderboarddict=bubble_sort(leaderboarddict,"score")

        #reverse
        leaderboarddict=list_reverse(leaderboarddict)

        for i in range(len(leaderboarddict)):
            leaderboardrecord.append(str(i+1)+". "+leaderboarddict[i]["nick"]+"  "+str(leaderboarddict[i]["score"])+" points  "+str(leaderboarddict[i]["time"])+" sec")
        for i in range(min(len(leaderboardrecord),10)):
            screen.blit(font.render(leaderboardrecord[i],True,(255,255,255)), (555, 200+i*50))
        fr.close()

    pygame.display.flip()
        