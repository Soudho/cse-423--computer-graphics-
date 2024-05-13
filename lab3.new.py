from OpenGL.GL import *
from OpenGL.GLUT import *
import random

s_width=500
s_height=600
bubble = []
bubble_speed = 0.5
for k in range(5):#create bubble randomly
    x = random.randint(50, s_width - 50)
    y = random.randint(s_height, s_height+250)
    r = random.randint(10, 20)
    bubble.append([x, y, r])

fire = []
fire_speed = 5
shooter_r = 20
shooter_x= 300
score = 0
lives_count = 3
shooter_y =40
flag_animate = True
flag_gameOver = False
flag_pause = False

def Int_FindZone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    zone = 0
    if abs(dx) > abs(dy):
        if dx>=0 and dy>0:
            zone = 0
        elif dx<=0 and dy>=0:
            zone = 3
        elif dx<0 and dy<0:
            zone = 4
        elif dx>0 and dy<0:
            zone = 7
    else:
        if dx >= 0 and dy > 0:
            zone = 1
        elif dx < 0 and dy > 0:
            zone = 2
        elif dx < 0 and dy < 0:
            zone = 5
        elif dx >= 0 and dy < 0:
            zone = 6
    return zone

def convertToZero(x,y,zone):
    if zone == 1:
        X, Y = y, x
    elif zone == 2:
        X, Y = y, -x
    elif zone == 3:
        X, Y = -x, y
    elif zone == 4:
        X, Y = -x, -y
    elif zone == 5:
        X, Y = -y, -x
    elif zone == 6:
        X, Y = -y, x
    elif zone == 7:
        X, Y = x, -y
    return int(X),int(Y)

def convertToOriginal(x,y,zone):
    if zone == 1:
        X, Y = y, x
    elif zone == 2:
        X, Y = -y, x
    elif zone == 3:
        X, Y = -x, y
    elif zone == 4:
        X, Y = -x, -y
    elif zone == 5:
        X, Y = -y, -x
    elif zone == 6:
        X, Y = y, -x
    elif zone == 7:
        X, Y = x, -y
    return int(X), int(Y)

def drawPoint(x, y, size=2):
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2f(int(x),int(y))
    glEnd()

def drawLine(x1, y1, x2, y2, color):#Midpoint line drawing algorithm <<To draw lines>>
    glColor3f(*color)
    zone = Int_FindZone(x1, y1, x2, y2)
    if zone != 0:
        x1, y1 = convertToZero(x1,y1,zone)
        x2, y2 = convertToZero(x2, y2, zone)

    dx = x2 - x1
    dy = y2 - y1
    d = 2*dy - dx
    incE = 2*dy
    incNE = 2*(dy-dx)
    y = y1

    for x in range(int(x1), int(x2)):
        if zone != 0:
            original_x, original_y = convertToOriginal(x, y, zone)
            drawPoint(original_x, original_y)
        else:
            drawPoint(x, y)

        if d>0:
            d = d + incNE
            y += 1
        else:
            d = d + incE

def draw_circle(r, value):
   global screen_height, screen_width

   d = 1-r
   x = 0
   y = r
   circle_points(x, y, value)
   while x<y:
       if d<0:
           d = d + 2*x + 3
           x = x + 1
       else:
           d = d + 2*x - 2*y + 5
           x = x + 1
           y = y - 1
       circle_points(x, y, value)

def circle_points(x, y, value):
    cx, cy  = value[0], value[1]
    drawPoint(x+cx, y+cy)
    drawPoint(y+cx, x+cy)
    drawPoint(y+cx, -x+cy)
    drawPoint(x+cx, -y+cy)
    drawPoint(-x+cx, -y+cy)
    drawPoint(-y+cx,-x+cy)
    drawPoint(-y+cx, x+cy)
    drawPoint(-x+cx, y+cy)

def draw_restart_button():#drawn through midpoint line drawing algorithm
    drawLine(20, s_height-30, 60, s_height-30, (0, 1, 1))
    drawLine(20, s_height-30, 30, s_height-40, (0, 1, 1))
    drawLine(20, s_height - 30, 30, s_height - 20, (0, 1, 1))


def draw_pause_button():#drawn through midpoint line drawing algorithm
    if flag_pause:
        drawLine(s_width//2 - 5, s_height - 20, s_width//2 - 5, s_height - 40, (0.7, 1, 0))
        drawLine(s_width//2 - 5, s_height - 20, s_width//2 + 15, s_height - 30, (0.7, 1, 0))
        drawLine(s_width // 2 - 5, s_height - 40, s_width // 2 + 15, s_height - 30, (0.7, 1, 0))

    else:
        drawLine(s_width // 2 + 5, s_height - 20, s_width // 2 + 5, s_height - 40, (1, 0.7, 0))
        drawLine(s_width//2 - 5, s_height - 20, s_width//2 - 5, s_height - 40, (1, 0.7, 0))


def draw_exit_button():#drawn through midpoint line drawing algorithm
    drawLine(s_width - 40, s_height - 40, s_width - 20, s_height - 20, (1, 0, 0))
    drawLine(s_width - 40, s_height - 20, s_width - 20, s_height - 40, (1, 0, 0))


def generate_bubble():
    global bubble
    x = random.randint(50, s_width - 50)
    y = s_height
    r = random.randint(10, 20)
    bubble.append([x, y, r])

def generate_fire():
    global shooter_x, shooter_y, shooter_r
    x = shooter_x
    y = shooter_y + shooter_r
    r = 5
    fire.append([x, y, r])

def draw_fire():
    global fire
    glColor3f(1, .1, 0)
    for i in fire:
        fire_x, fire_y, radius = i[0], i[1], i[2]
        draw_circle(radius, (fire_x, fire_y))

def draw_shooter():
    global shooter_x, shooter_y, shooter_r
    glColor3f(1,1,0)
    draw_circle(shooter_r, (shooter_x, shooter_y))

def draw_bubble():
    global bubble
    glColor3f(1, 1, 0)
    for i in bubble:
        bubble_x, bubble_y, radius = i[0], i[1], i[2]
        draw_circle(radius, (bubble_x, bubble_y))

def default_all():
    global s_width, s_height, shooter_x, shooter_y, shooter_r, bubble, bubble_speed, fire, fire_speed, \
        flag_gameOver, flag_pause, flag_animate, lives_count, score
    bubble = []
    bubble_speed = 1
    for i in range(5):
        x = random.randint(50, s_width - 50)
        y = random.randint(s_height, s_height + 250)
        r = random.randint(10, 20)
        bubble.append([x, y, r])
    fire = []
    fire_speed = 5
    score = 0
    lives_count = 3

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_restart_button()
    draw_pause_button()
    draw_exit_button()
    draw_shooter()
    draw_bubble()
    draw_fire()
    gameplay()
    glutSwapBuffers()

def animation():
    global bubble, bubble_speed
    if flag_animate:
        for i in bubble:
            i[1] -= bubble_speed
        for j in fire:
            j[1] += fire_speed

def gameplay():
    global s_width, s_height, shooter_x, shooter_y, shooter_r, bubble, bubble_speed, fire, fire_speed, \
        flag_gameOver, flag_pause, flag_animate, lives_count, score

    if not flag_pause and not flag_gameOver:
        flag_animate = True
        for i in bubble:
            bubble_y, bubble_r = i[1], i[2]
            if bubble_y == 0:
                lives_count -= 1
                print("lives left: ", lives_count)
                generate_bubble()
                if lives_count == 0:
                    bubble = []
                    flag_gameOver = True
                    flag_animate = False
                    print("game over")

        for i in range(len(bubble)):
            bubble_x, bubble_y, bubble_r = bubble[i][0], bubble[i][1], bubble[i][2]
            if bubble_x - bubble_r <= shooter_x <= bubble_x + bubble_r and bubble_y - bubble_r <= shooter_y <= bubble_y + bubble_r:
                flag_gameOver = True
                flag_animate = False
                print("game over")
                bubble = []
                break

        to_be_removed = []
        for i in range(len(bubble)):
            for j in range(len(fire)):
                bubble_x, bubble_y, bubble_r = bubble[i][0], bubble[i][1], bubble[i][2]
                fire_x, fire_y, fire_r = fire[j][0], fire[j][1], fire[j][2]
                if bubble_x - bubble_r <= fire_x <= bubble_x + bubble_r and bubble_y - bubble_r <= fire_y <= bubble_y + bubble_r:
                    to_be_removed.append((i, j))

        for i, j in to_be_removed:
            del bubble[i]
            del fire[j]

            score += 1
            print("Score: ",score)
            generate_bubble()

    glutPostRedisplay()


def mouse_click(button, state, x, y):
    global s_width, s_height, shooter_x, shooter_y, shooter_r, bubble, bubble_speed, fire, fire_speed, \
        flag_gameOver, flag_pause, flag_animate, lives_count, score

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        y = s_height - y

        # For exit
        if (s_width - 40 <= x <= s_width - 20) and (s_height - 40 <= y <= s_height - 20):
            print(f"Goodbye. Your Final Score: {score}")
            glutLeaveMainLoop()

        # For pause
        elif (s_width // 2 - 20 <= x <= s_width // 2 + 16) and (s_height - 50 <= y <= s_height - 10):
            if flag_gameOver == False:
                flag_pause = not flag_pause
                flag_animate = False

        # For restart
        elif (20 <= x <= 60) and (s_height - 50 <= y <= s_height - 10):
            print("Starting Over")

            flag_gameOver = False
            flag_pause = False
            default_all()


def keyboardListener(key, x, y):
    global shooter_x
    if not flag_pause and not flag_gameOver:
        move = 10
        if key == b'a':
            if shooter_x > 30:
                shooter_x -= move
        elif key == b'd':
            if shooter_x < s_width - 30:
                shooter_x += move
    if key == b' ':
        generate_fire()
    glutPostRedisplay()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(s_width, s_height)
glutCreateWindow(b"Shoot The Circles!")
glOrtho(0, s_width, 0, s_height, -1, 1)
glClearColor(0, 0, 0, 1)

glutDisplayFunc(display)
glutIdleFunc(animation)

glutMouseFunc(mouse_click)
glutKeyboardFunc(keyboardListener)
glutMainLoop()