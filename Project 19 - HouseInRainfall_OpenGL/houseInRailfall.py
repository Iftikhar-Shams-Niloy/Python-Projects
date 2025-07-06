from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time

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

def draw_lines(x1, y1, x2, y2):
    glPointSize(15)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def draw_square(x1, y1, x2, y2, x3, y3, x4, y4):
    glLineWidth(5.0)
    glPointSize(15)
    glBegin(GL_LINES)

    glVertex2f(x1, y1)
    glVertex2f(x2, y2)

    glVertex2f(x2-2, y2)
    glVertex2f(x3-2, y3)

    glVertex2f(x3, y3)
    glVertex2f(x4, y4)

    glVertex2f(x4+2, y4)
    glVertex2f(x1+2, y1)

    glEnd()

def draw_triangle(x1, y1, x2, y2, x3, y3):
    glLineWidth(5.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()

def draw_line_triangle(x1, y1, x2, y2, x3, y3):
    glLineWidth(10.0)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)

    glVertex2f(x2, y2)
    glVertex2f(x3, y3)

    glVertex2f(x3, y3)
    glVertex2f(x1, y1)
    glEnd()

def draw_windows(x1, y1, x2, y2, x3, y3, x4, y4):
    draw_square(x1, y1, x2, y2, x3, y3, x4, y4)
    x_new = round((x1 + x2) / 2)
    y_new = round((y1 + y3) / 2)

    glBegin(GL_LINES)
    glVertex2f(x_new, y1)
    glVertex2f(x_new, y3)

    glVertex2f(x1, y_new)
    glVertex2f(x2, y_new)
    glEnd()

def draw_quad(x1,y1, x2,y2, x3,y3, x4,y4):
    glBegin(GL_QUADS)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glVertex2f(x4,y4)
    glEnd()

x_cords=[0,25,50,75,100,
         125,150,175,200,
         225,250,275,300,
         325,350,375,400,
         425,450,475,500,
         525,550,575,600,
         625,650,675,700,
         725,750,775,800]
class Raindrop:
    def __init__(self):
        global x_cords
        self.x = random.choice(x_cords)
        self.y = random.uniform(0.0, 600.0)
        self.rainlength = random.uniform(20.0, 50.0)
        self.speedX = 0.0
        self.speedY = -5.0

raindrops = []
for i in range(200):
    raindrops.append(Raindrop())
backgroundColor = 0.0
rainDirection_X = 0.0
rainDirection_Y = 1.0

def drawRaindrops():
    global rainDirection_X
    glColor3f(0.0, 0.0, 0.6)
    glBegin(GL_LINES)
    for drop in raindrops:
        glVertex2f(drop.x, drop.y)
        glVertex2f(drop.x-(5*rainDirection_X),drop.y + drop.rainlength)
    glEnd()

def updateRaindrops():
    global x_cords
    global rainDirection_X

    for drop in raindrops:
        drop.x += drop.speedX + rainDirection_X
        drop.y += drop.speedY + rainDirection_Y
        if drop.y < 0.0:
            drop.y = 600.0
            drop.x = random.choice(x_cords)

def keyboard(key, x, y):
    global backgroundColor
    if key == b'1':
        backgroundColor += 0.01
        if backgroundColor > 1.0:
            backgroundColor = 1.0
    elif key == b'2':
        backgroundColor -= 0.01
        if backgroundColor < 0.0:
            backgroundColor = 0.0

def specialKeys(key, x, y):
    global rainDirection_X
    global rainDirection_Y
    if key == GLUT_KEY_LEFT:
        rainDirection_X -= 0.1
    elif key == GLUT_KEY_RIGHT:
        rainDirection_X += 0.1
    elif key == GLUT_KEY_UP:
        rainDirection_Y += 0.5
    elif key == GLUT_KEY_DOWN:
        rainDirection_Y -= 0.5

def timer(value):
    updateRaindrops()
    glutPostRedisplay()
    glutTimerFunc(16, timer, 0)

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

    R = 0.6
    G = 0.2
    B = 0.3
    for i in range(20):
        R += 0.01
        G += 0.01
        B += 0.01
        glColor3f(R,G,B)
        draw_square(200+i,50+i,
                    600+i,50+i,
                    600+i,250+i,
                    200+i,250+i)
    glColor3f(0.6, 0.2, 0.3)
    draw_square(200, 50,
                600, 50,
                600, 250,
                200, 250)

    R = 0.1
    G = 0.4
    B = 0.2
    for i in range(20):
        R += 0.01
        G += 0.01
        B += 0.01
        glColor3f(R,G,B)
        draw_line_triangle(190+i,250+i,
                           610+i,250+i,
                           400+i,400+i)
    glColor3f(0.1, 0.4, 0.2)
    draw_line_triangle(190, 250,
                       610, 250,
                       400, 400)

    glColor3f(0.5, 0.4, 0.3)
    draw_quad(260,75,
                340,75,
                340,185,
                260,185)
    glColor3f(0.3,0.2,0.1)
    draw_square(260, 75,
                340, 75,
                340, 185,
                260, 185)

    draw_smooth_points(320.00, 130.00)

    glColor3f(0.5, 0.4, 0.3)
    draw_quad(450, 120,
             540, 120,
             540, 200,
             450, 200)
    glColor3f(0.3,0.2,0.1)

    n = 1
    glColor3f(0.3,0.2,0.1)
    for i in range(10):
        R = 0.3 + n*0.01
        G = 0.2 +  n*0.01
        B = 0.1 + n*0.01
        glColor3f(R,G,B)
        draw_windows(451-n, 121-n,
                     541-n, 121-n,
                     541-n, 201-n,
                     451-n, 201-n)
        n+= 1

    drawRaindrops()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"House In Rainfall")
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)
    glutSpecialFunc(specialKeys)
    glutKeyboardFunc(keyboard)
    glutTimerFunc(16, timer, 0) #FPS
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 800.0, 0.0, 600.0)
    glutMainLoop()

if __name__ == "__main__":
    main()
