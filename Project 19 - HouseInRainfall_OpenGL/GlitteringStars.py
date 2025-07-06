from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time

NUMBER_OF_STARS = 20
W_WIDTH = 500
W_HEIGHT = 500
STAR_MOVE = False
STAR_GLITTER = True
STAR_BLINK = False

class Stars:
    def __init__(self):
        switch = [True,False]
        self.size = random.randint(2,9)
        self.x = random.randint(100,400)
        self.y = random.randint(100,400)
        self.direction_X = random.randint(-3,3)
        self.direction_Y = random.randint(-3,3)
        self.red = random.uniform(0.1,1.0)
        self.blue = random.uniform(0.1,1.0)
        self.green = random.uniform(0.1,1.0)
        self.getBig = random.choice(switch)

stars = []

for i in range(NUMBER_OF_STARS):
    stars.append(Stars())

backgroundColor = 0.0
def draw_points(x, y):
    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def draw_smooth_points(x, y):
    glEnable(GL_POINT_SMOOTH)
    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glDisable(GL_POINT_SMOOTH)

def drawStars():
    for star in stars:
        glEnable(GL_POINT_SMOOTH)
        glPointSize(star.size)
        glColor3f(star.red, star.green, star.blue)
        glBegin(GL_POINTS)
        glVertex2f(star.x, star.y)
        glEnd()
        glDisable(GL_POINT_SMOOTH)

def updateStars():
    global backgroundColor
    global stars,STAR_MOVE, STAR_GLITTER

    if STAR_GLITTER == True:
        for star in stars:
            if star.getBig == True:
                if star.size >= 10:
                    star.getBig = False
                else:
                    star.size += 1
            else:
                if star.size <= 1:
                    star.getBig = True
                else:
                    star.size -= 1

    if STAR_MOVE == True:
        for star in stars:
            star.x += star.direction_X
            star.y += star.direction_Y
            if star.x > 500 or star.x < 0:
                star.direction_X = -star.direction_X
            if star.y > 500 or star.y < 0:
                star.direction_Y = -star.direction_Y

def convert_coordinate(x,y):
    global W_WIDTH, W_HEIGHT
    a = x - (W_WIDTH/2)
    b = (W_HEIGHT/2) - y
    return a,b

def mouseListener(button,state,x,y):  # /#/x, y is the x-y of the screen (2D)
    global stars
    global STAR_MOVE, STAR_GLITTER, STAR_BLINK
    if button == GLUT_LEFT_BUTTON:
        if STAR_GLITTER == True:
            STAR_GLITTER = False
        else:
            STAR_GLITTER = True

        if STAR_BLINK == True:
            STAR_BLINK = False
        else:
            STAR_BLINK = True

        if STAR_BLINK == True:
            for star in stars:
                star.red=backgroundColor
                star.green=backgroundColor
                star.blue=backgroundColor
        else:
            for star in stars:
                star.red=random.uniform(0.1,1.0)
                star.blue=random.uniform(0.1,1.0)
                star.green=random.uniform(0.1,1.0)

    if button == GLUT_RIGHT_BUTTON:
        STAR_MOVE = True
        stars.clear()
        stars = []
        for i in range(NUMBER_OF_STARS):
            stars.append(Stars())

def keyboard(key, x, y):
    global backgroundColor
    global STAR_MOVE, STAR_GLITTER
    if key == b'1':
        backgroundColor += 0.01
        if backgroundColor > 1.0:
            backgroundColor = 1.0
    elif key == b'2':
        backgroundColor -= 0.01
        if backgroundColor < 0.0:
            backgroundColor = 0.0
    elif key == b' ':
        if STAR_MOVE == False and STAR_GLITTER == False:
            STAR_MOVE = True
            STAR_GLITTER = True
        else:
            STAR_MOVE = False
            STAR_GLITTER = False

def specialKeys(key, x, y):
    global stars
    global STAR_MOVE, STAR_GLITTER
    if key == GLUT_KEY_LEFT:
        pass
    elif key == GLUT_KEY_RIGHT:
        pass
    elif key == GLUT_KEY_UP:
        for star in stars:
            if star.direction_X >= 0:
                star.direction_X +=1
            else:
                star.direction_X -= 1
            if star.direction_Y >= 0:
                star.direction_Y += 1
            else:
                star.direction_Y -= 1
    elif key == GLUT_KEY_DOWN:
        for star in stars:
            if star.direction_X >= 0:
                star.direction_X -=1
            else:
                star.direction_X += 1
            if star.direction_Y >= 0:
                star.direction_Y -= 1
            else:
                star.direction_Y += 1


def timer(value):
    glutPostRedisplay()
    updateStars()
    glutTimerFunc(30, timer, 0)

def iterate():
    glViewport(0, 0, 800, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 800.0, 0.0, 600.0, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    global backgroundColor
    glClearColor(backgroundColor, backgroundColor, backgroundColor, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    drawStars()

    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Glittering Stars")
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)

    glutSpecialFunc(specialKeys)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(mouseListener)

    glutTimerFunc(30, timer, 0) #FPS
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 800.0, 0.0, 600.0)
    glutMainLoop()

if __name__ == "__main__":
    main()
