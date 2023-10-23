

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

times = int(input("Enter how many circle you want : "))
def draw_point(x, y):
   glPointSize(5)
   glBegin(GL_POINTS)
   glVertex2f(x, y)
   glEnd()


##########################################

def Pixel(x,y,h,k):

   # zone1
   a = x + h
   b = y + k
   draw_point(a, b)

   # zone0
   a = y + h
   b = x + k
   draw_point(a, b)

   # zone2
   a = -x + h
   b = y + k
   draw_point(a, b)

   # zone3
   a = -y + h
   b = x + k
   draw_point(a, b)

   # zone4
   a = -y + h
   b = -x + k
   draw_point(a, b)

   # zone5
   a = -x + h
   b = -y + k
   draw_point(a, b)

   # zone6
   a = x + h
   b = -y + k
   draw_point(a, b)

   # zone7
   a = y + h
   b = -x + k
   draw_point(a, b)



##########################################



def iterate():
   glViewport(0, 0, 500, 500)
   glMatrixMode(GL_PROJECTION)
   glLoadIdentity()
   glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
   glMatrixMode(GL_MODELVIEW)
   glLoadIdentity()



def showScreen():
   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   glLoadIdentity()
   iterate()
   glColor3f(1.0, 3.0, 2.0)
   ############
   count = 0
   if count < times:
       count+=1
       h = 250
       k = 250
       r = 200
       # h=int(input("H: "))
       # k = int(input("k: "))
       # r = int(input("r: "))

       x = 0
       y = r
       d = 1 - r
       while x < y:
           Pixel(x, y, h, k)
           if d > 0:
               d = d + (2 * x) - (2 * y) + 5
               x = x + 1
               y = y - 1
           elif d <= 0:
               d = d + (2 * x) + 3
               x = x + 1
               y = y
   if count < times:
       count += 1
       h1 = h
       k1 = k
       r1 = r
    # up
       h = h1
       k = (k1 + (r1 / 2))
       r = (r1 / 2)
       # print(h,k,r)
       x = 0
       y = r
       d = 1 - r
       while x < y:
           Pixel(x, y, h, k)
           if d > 0:
               d = d + (2 * x) - (2 * y) + 5
               x = x + 1
               y = y - 1
           elif d <= 0:
               d = d + (2 * x) + 3
               x = x + 1
               y = y

   #down
   if count < times:
       count += 1
   h = h1
   k = k1-(r1/2)
   r = (r1 / 2)
   # print(h,k,r)
   x = 0
   y = r
   d = 1 - r
   while x < y:
       Pixel(x, y, h, k)
       if d > 0:
           d = d + (2 * x) - (2 * y) + 5
           x = x + 1
           y = y - 1
       elif d <= 0:
           d = d + (2 * x) + 3
           x = x + 1
           y = y


   ##Right
   if count < times:
       count += 1
       h = h1 + (r1 / 2)
       k = k1
       r = (r1 / 2)
       # print(h,k,r)
       x = 0
       y = r
       d = 1 - r
       while x < y:
           Pixel(x, y, h, k)
           if d > 0:
               d = d + (2 * x) - (2 * y) + 5
               x = x + 1
               y = y - 1
           elif d <= 0:
               d = d + (2 * x) + 3
               x = x + 1
               y = y


   ##Left
   if count < times:
       count += 1
       h = h1 - (r1 / 2)
       k = k1
       r = (r1 / 2)
       # print(h,k,r)
       x = 0
       y = r
       d = 1 - r
       while x < y:
           Pixel(x, y, h, k)
           if d > 0:
               d = d + (2 * x) - (2 * y) + 5
               x = x + 1
               y = y - 1
           elif d <= 0:
               d = d + (2 * x) + 3
               x = x + 1
               y = y

   #diagonal right up
   if count < times:
       count += 1
       c1 = ((r * 1.376) + (h1 + k1)) / 2
       h = c1
       k = c1
       # print(c1,h,k)
       r = (r1 / 2)
       # print(h,k,r)
       x = 0
       y = r
       d = 1 - r
       while x < y:
           Pixel(x, y, h, k)
           if d > 0:
               d = d + (2 * x) - (2 * y) + 5
               x = x + 1
               y = y - 1
           elif d <= 0:
               d = d + (2 * x) + 3
               x = x + 1
               y = y

   # diagonal left down
   if count < times:
       count += 1
       c2 = ((r * 1.376) - (h1 + k1)) / 2
       h = -c2
       k = -c2
       # print(c2, h, k)
       r = (r1 / 2)
       # print(h,k,r)
       x = 0
       y = r
       d = 1 - r
       while x < y:
           Pixel(x, y, h, k)
           if d > 0:
               d = d + (2 * x) - (2 * y) + 5
               x = x + 1
               y = y - 1
           elif d <= 0:
               d = d + (2 * x) + 3
               x = x + 1
               y = y


   # diagonal left up
   if count < times:
       count += 1
       c = ((r * 1.376) + (h1 + k1)) / 2
       h = -c2
       k = c1
       # print(c, h, k)
       r = (r1 / 2)
       # print(h,k,r)
       x = 0
       y = r
       d = 1 - r
       while x < y:
           Pixel(x, y, h, k)
           if d > 0:
               d = d + (2 * x) - (2 * y) + 5
               x = x + 1
               y = y - 1
           elif d <= 0:
               d = d + (2 * x) + 3
               x = x + 1
               y = y

   # diagonal right down
   if count < times:
       count += 1
       c = ((r * 1.376) - (h1 + k1)) / 2
       h = c1
       k = -c2
       # print(c, h, k)
       r = (r1 / 2)
       # print(h,k,r)
       x = 0
       y = r
       d = 1 - r
       while x < y:
           Pixel(x, y, h, k)
           if d > 0:
               d = d + (2 * x) - (2 * y) + 5
               x = x + 1
               y = y - 1
           elif d <= 0:
               d = d + (2 * x) + 3
               x = x + 1
               y = y

   glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")  # window name
glutDisplayFunc(showScreen)

glutMainLoop()
