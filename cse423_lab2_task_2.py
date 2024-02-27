from OpenGL.GL import*
from OpenGL.GLUT import*
from OpenGL.GLU import*
import random
import time
start_time=time.time()

def drawPoint(x, y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()
catcher = [[-15,-150,-20,-140],[-15,-150,15,-150],[-20,-140,20,-140],[15,-150,20,-140]]
diamond = [[0,140,-5,135],[0,140,5,135],[0,130,-5,135],[0,130,5,135]]

speed = 1
play=False
freeze= False
diamondColor= [1.0, 1.0, 1.0]
whiteColor= [1.0, 1.0, 1.0]
catcherColor= [1.0, 1.0, 1.0]
score= 0


def newdiamond():
    global diamondColor
    global diamond
    diamondColor=[random.random(),random.random(),random.random()]
    p=random.randrange(-140,140)
    diamond=[[p,140,p+5,135],[p,140,p-5,135],[p,130,p-5,135],[p,130,p+5,135]]
def fallofdiamond():
    global speed
    global diamond
    global catcher
    global score
    global freeze
    if (not freeze):
        diamond[0][1]-=speed
        diamond[0][3]-=speed
        diamond[1][1]-=speed
        diamond[1][3]-=speed
        diamond[2][1]-=speed
        diamond[2][3]-=speed
        diamond[3][1]-=speed
        diamond[3][3]-=speed
        if (((diamond[1][2]>=catcher[0][2] and diamond[1][2]-5<=catcher[2][2])or (diamond[0][2]>=catcher[0][2] and diamond[0][2]<=catcher[2][2]) )and diamond[2][1]<catcher[0][3]):
            score+=1
            print("SCORE:",score)
            print(speed)
            newdiamond()
        elif (((diamond[1][2]<catcher[1][2]) or (diamond[0][2]>catcher[1][2])) and diamond[2][1]<catcher[0][3]):#checking the boundary issue of the catcher
            print("Game Over! Score:", score)
            score = 0
            freeze = True
            gameOver()


def gameOver():
    global catcherColor
    global score
    global speed
    catcherColor = [1.0, 0, 0]
    score = 0
    speed=1
def playPause(freeze):
    if freeze:
        midpointline(-20,135,-20,143)
        midpointline(-20,135,15,140)
        midpointline(-20,143,15,140)
    else:
        midpointline(-10,135,-10,145)
        midpointline(10,135,10,145)


def findzone(x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1
    if abs(dx)>=abs(dy):
        if dx>=0 and dy>=0:
            return 0
        elif dx<=0 and dy>=0:
            return 3
        elif dx>=0 and dy<=0:
            return 7
        elif dx<=0 and dy<=0:
            return 4
    else:
        if dy>=0 and dx>=0:
            return 1
        elif dy>=0 and dx<=0:
            return 2
        elif dy<=0 and dx>=0:
            return 6
        elif dy<=0 and dx<=0:
            return 5

def Zone0converter(x,y,zone):
    if zone ==0:
        return x,y
    elif zone ==1:
        return y,x
    elif zone ==2:
        return y,-x
    elif zone ==3:
        return -x,y
    elif zone ==4:
        return -x,-y
    elif zone ==5:
        return  -y,-x
    elif zone ==6:
        return -y,x
    elif zone ==7:
        return  x,-y

def convertTOOrginalzone(x,y,zone):
    if zone==0:
        return x,y
    elif zone==1:
        return y,x
    elif zone==2:
        return -y,x
    elif zone==3:
        return -x,y
    elif zone==4:
        return -x,-y
    elif zone==5:
        return -y,-x
    elif zone==6:
        return y,-x
    else:
        return x,-y

def midpointline(x1,y1,x2,y2):
    zone = findzone(x1,y1,x2,y2)
    x1,y1= Zone0converter(x1,y1,zone)
    x2,y2 = Zone0converter(x2,y2,zone)
    dx=x2-x1
    dy=y2-y1
    d=2*dy-dx
    delE=2*dy
    delNE=2*(dy-dx)
    a=x1
    b=y1
    while (a <= x2):
        x_original, y_original = convertTOOrginalzone(a, b, zone)
        drawPoint(x_original, y_original)
        a+=1
        if d > 0:
            d += delNE
            b+=1
        else:
            d += delE

def specialKey(key,x,y):
    global freeze
    if (not freeze):
        if key==GLUT_KEY_LEFT:
            for j in range(4):
                catcher[j][0]-= 10
                catcher[j][2]-=10
            if catcher[2][0]<-150:
                for j in range(4):
                    catcher[j][0]+=10
                    catcher[j][2]+=10
        elif key==GLUT_KEY_RIGHT:
            for k in range(4):
                catcher[k][0]+=10
                catcher[k][2]+=10
            if catcher[2][2]>150:
                for i in range(4):
                    catcher[i][0]-=10
                    catcher[i][2]-=10

def anotherfunction(button,st,x,y):
    global play
    global freeze
    global score
    global catcherColor
    global whiteColor
    if button==GLUT_LEFT_BUTTON and st==GLUT_DOWN:
        if ((100<=x<=250) and (0<=y<=50)):
            play = not play
            freeze = not freeze
        elif ((0<x<65) and (0<=y<=50)):
            # reset
            print("Starting Over!")
            freeze = False
            catcherColor = [whiteColor[0], whiteColor[1], whiteColor[2]]
            newdiamond()
        elif ((251<=x<=400) and (0<=y<=50)):
            print("Goodbye! Score:", score)
            glutLeaveMainLoop()


def init():
    glClearColor(0, 0, 0, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-150, 150, -150, 150)
def display():
    global freeze
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(*catcherColor)
    midpointline(catcher[0][0],catcher[0][1],catcher[0][2],catcher[0][3])
    midpointline(catcher[1][0], catcher[1][1], catcher[1][2],catcher[1][3])
    midpointline(catcher[2][0], catcher[2][1], catcher[2][2],catcher[2][3])
    midpointline(catcher[3][0], catcher[3][1], catcher[3][2],catcher[3][3])

    glColor3f(*diamondColor)
    midpointline(diamond[0][0], diamond[0][1], diamond[0][2], diamond[0][3])
    midpointline(diamond[1][0], diamond[1][1], diamond[1][2], diamond[1][3])
    midpointline(diamond[2][0], diamond[2][1], diamond[2][2], diamond[2][3])
    midpointline(diamond[3][0], diamond[3][1], diamond[3][2], diamond[3][3])

    #reset button
    glColor3f(1/255,139/255,120/255)
    midpointline(-140,140,-110,140)
    midpointline(-140, 140, -125, 145)
    midpointline(-140, 140, -120, 135)
    #play pause button
    glColor3f(255/255,191/255,0/255)
    playPause(freeze)
    #Close button
    glColor3f(1,0,0)
    midpointline(145,145,135,135)
    midpointline(135,145,145,135)
    # displaydiamond()



    glutSwapBuffers()
def animate():
    glutPostRedisplay()
def update(value):
    global speed
    global start_time
    elapsed_time=time.time()-start_time
    if elapsed_time>=10:
        speed+=1
        start_time=time.time()
    fallofdiamond()
    glutTimerFunc(10, update, 0)
    glutPostRedisplay()

glutInit()
glutInitWindowSize(400, 700)
glutInitWindowPosition(200, 350)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutCreateWindow(b"Catch The Diamonds")
glutDisplayFunc(display)
init()
glutTimerFunc(25, update, 0)
glutSpecialFunc(specialKey)
glutMouseFunc(anotherfunction)
glutIdleFunc(animate)
glutMainLoop()





