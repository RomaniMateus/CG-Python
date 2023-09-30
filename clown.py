from OpenGL.GL import *
from OpenGL.GLUT import *

window_width = 800
window_height = 800

theta_x = 0.0
theta_y = 0.0
theta_z = 0.0


def draw_sphere(radius):
    glPushMatrix()
    glutSolidSphere(radius, 100, 100)
    glPopMatrix()


def keyboard(key, x, y):
    global theta_x, theta_y, theta_z

    if key == b" ":
        car_x = 0.0
    elif key == GLUT_KEY_LEFT:
        theta_y -= 1.0
    elif key == GLUT_KEY_RIGHT:
        theta_y += 1.0
    elif key == GLUT_KEY_UP:
        theta_x -= 1.0
    elif key == GLUT_KEY_DOWN:
        theta_x += 1.0

    glutPostRedisplay()  # Trigger a redraw


def timer_func(value):
    glutPostRedisplay()
    glutTimerFunc(10, timer_func, 0)


class Hair:
    def __init__(self, x, y, z, red=0.439, green=0.384, blue=0.988):
        self.x = x
        self.y = y
        self.z = z
        self.red = red
        self.green = green
        self.blue = blue

    def draw(self):
        glColor3f(self.red, self.green, self.blue)
        glPushMatrix()
        glRotatef(theta_x, 1, 0, 0)
        glRotatef(theta_y, 0, 1, 0)
        glRotatef(theta_z, 0, 0, 1)
        glTranslatef(self.x, self.y, self.z)
        draw_sphere(0.17)
        glPopMatrix()


class Head:
    def __init__(self, radius, red, green, blue):
        self.radius = radius
        self.red = red
        self.green = green
        self.blue = blue

    def draw(self):
        global theta_x, theta_y, theta_z

        glPushMatrix()
        glColor3f(self.red, self.green, self.blue)
        glRotatef(0.5 + theta_x, 1, 0, 0)
        glRotatef(0.5 + theta_y, 0, 1, 0)
        glRotatef(0.5 + theta_z, 0, 0, 1)
        draw_sphere(self.radius)
        glPopMatrix()


class Hat:
    def __init__(self, red=1, green=0.655, blue=0, x=0, y=0.4, z=0, rotation_angle=-90):
        self.red = red
        self.green = green
        self.blue = blue
        self.x = x
        self.y = y
        self.z = z
        self.rotation_angle = rotation_angle

    def draw(self):
        glColor3f(self.red, self.green, self.blue)

        glPushMatrix()
        glRotatef(theta_x, 1, 0, 0)
        glRotatef(theta_y, 0, 1, 0)
        glRotatef(theta_z, 0, 0, 1)
        glTranslatef(self.x, self.y, self.z)
        glRotatef(self.rotation_angle, 1, 0, 0)
        glutSolidCone(0.3, 0.55, 100, 100)
        glPopMatrix()


class Eye:
    def __init__(self, x, y, z, red=0, green=0, blue=0, radius=0.05):
        self.x = x
        self.y = y
        self.z = z
        self.red = red
        self.green = green
        self.blue = blue
        self.radius = radius

    def draw(self):
        glColor3f(self.red, self.green, self.blue)
        glPushMatrix()
        glRotatef(theta_x, 1, 0, 0)
        glRotatef(theta_y, 0, 1, 0)
        glRotatef(theta_z, 0, 0, 1)
        glTranslatef(self.x, self.y, self.z)
        draw_sphere(self.radius)
        glPopMatrix()


class Nose:
    def __init__(self, x, y, z, red=1.0, green=0.0, blue=0.0, radius=0.2):
        self.x = x
        self.y = y
        self.z = z
        self.red = red
        self.green = green
        self.blue = blue
        self.radius = radius

    def draw(self):
        glColor3f(self.red, self.green, self.blue)
        glPushMatrix()
        glRotatef(theta_x, 1, 0, 0)
        glRotatef(theta_y, 0, 1, 0)
        glRotatef(theta_z, 0, 0, 1)
        glTranslatef(self.x, self.y, self.z)
        draw_sphere(self.radius)
        glPopMatrix()


class Clown:
    def __init__(self):
        self.hair = []
        self.head = None
        self.hat = None
        self.eye = []
        self.nose = None

        self.hair.append(Hair(0.3, 0.19, 0.36))
        self.hair.append(Hair(0.27, 0.38, 0.17))
        self.hair.append(Hair(0.45, 0.11, 0.2))
        self.hair.append(Hair(0.43, 0.25, -0.06))
        self.hair.append(Hair(0.24, 0.42, -0.14))
        self.hair.append(Hair(0.32, 0.23, -0.31))
        self.hair.append(Hair(0.44, 0.02, -0.23))
        self.hair.append(Hair(-0.1, 0.46, 0.17))
        self.hair.append(Hair(-0.09, 0.44, -0.23))
        self.hair.append(Hair(0.04, 0.22, -0.45))
        self.hair.append(Hair(-0.44, 0.34, 0))
        self.hair.append(Hair(-0.32, 0.26, -0.28))
        self.hair.append(Hair(-0.12, -0.02, -0.49))
        self.hair.append(Hair(0.2, 0, -0.46))
        self.hair.append(Hair(-0.49, 0.04, -0.09))
        self.hair.append(Hair(-0.39, -0.15, -0.28))

        self.head = Head(0.5, 1, 1, 1)
        self.hat = Hat()

        self.eye.append(Eye(-0.15, 0.11, 0.46))
        self.eye.append(Eye(0.15, 0.11, 0.46))

        self.nose = Nose(0.0, -0.15, 0.47)

    def draw(self):
        global theta_x, theta_y, theta_z

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        glMatrixMode(GL_MODELVIEW)

        self.head.draw()

        for hair in self.hair:
            hair.draw()

        for eye in self.eye:
            eye.draw()

        self.nose.draw()

        self.hat.draw()

        theta_x += 0.1
        theta_y += 0.1
        theta_z += 0.1

        glutSwapBuffers()


def main():
    clown = Clown()

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

    glutInitWindowSize(window_width, window_height)
    glutCreateWindow("Clown")

    glutDisplayFunc(clown.draw)
    glutIdleFunc(clown.draw)
    glutTimerFunc(0, timer_func, 0)
    glEnable(GL_DEPTH_TEST)
    glutSpecialFunc(keyboard)  # Register the keyboard function for standard keys
    glutMainLoop()


if __name__ == "__main__":
    main()
