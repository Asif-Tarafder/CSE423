from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
num = input("Enter your id:")
def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def original_zone(x,y,zone): #zone0

    if zone == 1:
        x, y = y, x
    elif zone == 2:
        x, y = -y, x
    elif zone == 3:
        x, y = -x, y
    elif zone == 4:
        x, y = -x, -y
    elif zone == 5:
        x, y = -y, -x
    elif zone == 6:
        x, y = y, x
    elif zone == 7:
        x, y = x, -y
    draw_points(x, y)
def midpoint_algorithm(x0,y0,x1,y1):
    dx = x1 - x0  # STEP 1
    dy = y1 - y0
    zone = 0
    ##zone 0 and zone1 --> FINDING ZONE
    if dx >= 0 and dy >= 0:
        if abs(dx) > abs(dy):
            zone = 0
        elif abs(dx) < abs(dy):
            zone = 1
        # zone23
    if dx < 0 and dy >= 0:
        if abs(dx) > abs(dy):
            zone = 3
        elif abs(dx) < abs(dy):
            zone = 2

        # zone45
    if dx < 0 and dy < 0:
        if abs(dx) > abs(dy):
            zone = 4
        elif abs(dx) < abs(dy):
            zone = 5

        # zone67
    if dx > 0 and dy < 0:
        if abs(dx) >= abs(dy):
            zone = 7
        elif abs(dx) < abs(dy):
            zone = 6
    ##conversion to zone 0
    if zone == 1:
        x0, y0 = y0, x0
        x1, y1 = y1, x1

    elif zone == 2:
        x0, y0 = y0, -x0
        x1, y1 = y1, -x1

    elif zone == 3:
        x0, y0 = -x0, -y0
        x1, y1 = -x1, -y1

    elif zone == 4:

        x0, y0 = -x0, -y0
        x1, y1 = -x1, -y1

    elif zone == 5:
        x0, y0 = -y0, -x0
        x1, y1 = -y1, -x1

    elif zone == 6:
        x0, y0 = -y0, x0
        x1, y1 = -y1, x1

    elif zone == 7:
        x0, y0 = x0, -y0
        x1, y1 = x1, -y1
    # zone 0 pixels

    dx = x1 - x0
    dy = y1 - y0

    d = 2 * dy - dx  # d_initial=2dy-dx
    x = x0
    y = y0
    original_zone(x, y, zone)
    while (x <= x1):

        if (d > 0):
            d = d + (2 * dy) - (2 * dx)
            x = x + 1
            y = y + 1
        else:
            d = d + (2 * dy)
            x = x + 1
        original_zone(x, y, zone)

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.5, 0.5) #konokichur color set (RGB)
    #call the draw methods here

    x0 = 50
    y0 = 50
    x1 = 50
    y1 = 450
    midpoint_algorithm(x0,y0,x1,y1)
    midpoint_algorithm(50, 450, 200, 450)
    midpoint_algorithm(200, 50, 200, 450)
    midpoint_algorithm(50, 50, 200, 50)
    midpoint_algorithm(300, 450, 450, 450)
    midpoint_algorithm(300, 50, 300, 450)
    midpoint_algorithm(300, 50, 450, 50)
    midpoint_algorithm(450, 50, 450, 450)
    midpoint_algorithm(300, 250, 450, 250)


    glutSwapBuffers()
def showScreen2():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.5, 0.5) #konokichur color set (RGB)
    #call the draw methods here

    x0 = 50
    y0 = 50
    x1 = 50
    y1 = 450
    if num[-2] == "0":
        midpoint_algorithm(x0, y0, x1, y1)
        midpoint_algorithm(50, 450, 200, 450)
        midpoint_algorithm(200, 50, 200, 450)
        midpoint_algorithm(50, 50, 200, 50)

    if num[-1] == "0":
        midpoint_algorithm(x0, y0, x1, y1)
        midpoint_algorithm(250, 450, 400, 450)
        midpoint_algorithm(400, 50, 250, 450)
        midpoint_algorithm(250, 50, 400, 50)

    if num[-1] == "1":
        midpoint_algorithm(300, 50, 300, 450)

    if num[-2] == "1":
        midpoint_algorithm(50, 50, 50, 450)
    if num[-1] == "2":
        midpoint_algorithm(300, 450, 450, 450)
        midpoint_algorithm(450, 250, 450, 450)
        midpoint_algorithm(300, 250, 450, 250)
        midpoint_algorithm(300, 50, 300, 250)
        midpoint_algorithm(300, 50, 450, 50)
    if num[-2] == "2":
        midpoint_algorithm(50, 450, 200, 450)
        midpoint_algorithm(200, 250, 200, 450)
        midpoint_algorithm(50, 250, 200, 250)
        midpoint_algorithm(50, 50, 50, 250)
        midpoint_algorithm(50, 50, 200, 50)
    if num[-1] == "3":
        midpoint_algorithm(300, 450, 450, 450)
        midpoint_algorithm(450, 250, 450, 450)
        midpoint_algorithm(300, 250, 450, 250)
        midpoint_algorithm(450, 50, 450, 250)
        midpoint_algorithm(300, 50, 450, 50)
    if num[-2] == "3":
        midpoint_algorithm(50, 450, 200, 450)
        midpoint_algorithm(200, 250, 200, 450)
        midpoint_algorithm(50, 250, 200, 250)
        midpoint_algorithm(200, 50, 200, 250)
        midpoint_algorithm(50, 50, 200, 50)
    if num[-1] == "4":
        midpoint_algorithm(300, 250, 300, 450)
        midpoint_algorithm(300, 250, 450, 250)
        midpoint_algorithm(450, 50, 450, 250)
        midpoint_algorithm(450, 250, 450, 300)
    if num[-2] == "4":
        midpoint_algorithm(50, 250, 50, 450)
        midpoint_algorithm(50, 250, 200, 250)
        midpoint_algorithm(200, 50, 200, 250)
        midpoint_algorithm(200, 250, 200, 300)
    if num[-1] == "5":
        midpoint_algorithm(300, 450, 450, 450)
        midpoint_algorithm(300, 250, 300, 450)
        midpoint_algorithm(300, 250, 450, 250)
        midpoint_algorithm(450, 50, 450, 250)
        midpoint_algorithm(300, 50, 450, 50)
    if num[-2] == "5":
        midpoint_algorithm(50, 450, 200, 450)
        midpoint_algorithm(50, 250, 50, 450)
        midpoint_algorithm(50, 250, 200, 250)
        midpoint_algorithm(200, 50, 200, 250)
        midpoint_algorithm(50, 50, 200, 50)

    if num[-2] == "6":
        midpoint_algorithm(50, 450, 200, 450)
        midpoint_algorithm(50, 50, 50, 450)
        midpoint_algorithm(50, 50, 200, 50)
        midpoint_algorithm(200, 50, 200, 250)
        midpoint_algorithm(50, 250, 200, 250)
    if num[-1] == "6":
        midpoint_algorithm(300, 450, 450, 450)
        midpoint_algorithm(300, 50, 300, 450)
        midpoint_algorithm(300, 50, 450, 50)
        midpoint_algorithm(450, 50, 450, 250)
        midpoint_algorithm(300, 250, 450, 250)

    if num[-1] == "7":
        midpoint_algorithm(300, 450, 450, 450)
        midpoint_algorithm(450, 450, 300, 50)

    if num[-2] == "7":
        midpoint_algorithm(50, 450, 200, 450)
        midpoint_algorithm(200, 450, 50, 50)

    if num[-2] == "8":
        midpoint_algorithm(50, 450, 200, 450)
        midpoint_algorithm(50, 50, 50, 450)
        midpoint_algorithm(50, 50, 200, 50)
        midpoint_algorithm(200, 50, 200, 450)
        midpoint_algorithm(50, 250, 200, 250)
    if num[-1] == "8":
        midpoint_algorithm(300, 450, 450, 450)
        midpoint_algorithm(300, 50, 300, 450)
        midpoint_algorithm(300, 50, 450, 50)
        midpoint_algorithm(450, 50, 450, 450)
        midpoint_algorithm(300, 250, 450, 250)
    if num[-2] == "9":
        midpoint_algorithm(50, 450, 200, 450)
        midpoint_algorithm(50, 250, 50, 450)
        midpoint_algorithm(200, 50, 200, 450)
        midpoint_algorithm(50, 250, 200, 250)
        midpoint_algorithm(50, 50, 200, 50)
    if num[-1] == "9":
        midpoint_algorithm(300, 450, 450, 450)
        midpoint_algorithm(300, 250, 300, 450)
        midpoint_algorithm(450, 50, 450, 450)
        midpoint_algorithm(300, 250, 450, 250)
        midpoint_algorithm(300, 50, 450, 50)
















    glutSwapBuffers()


#num = input("Enter a number: ")
#l = [50,50,50,450,50,450,200,450]
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
#if num=="2":
 #   glutDisplayFunc(showScreen)
  #  glutMainLoop()
#else:
glutDisplayFunc(showScreen2)
glutMainLoop()