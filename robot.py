from OpenGL.GL import *
from OpenGL.GLUT import *
import math

# Window dimensions
window_width = 800
window_height = 600

rotation_angle = 0.0

body_x = 0.0
body_y = 0.0

rotation_increment = 180


def draw_upper_body():
    glColor3f(0.235, 0.431, 0.392)
    glRectf(body_x - 0.2, body_y - 0.5, body_x + 0.2, body_y + 0.1)


def draw_right_arm():
    glColor3f(0.176, 0.443, 0.6)
    glRectf(body_x + 0.32, body_y - 0.3, body_x + 0.2, body_y - 0.01)


def draw_left_arm():
    glColor3f(0.176, 0.443, 0.6)
    glRectf(body_x - 0.32, body_y - 0.3, body_x - 0.2, body_y - 0.01)


def draw_head():
    glColor3f(0.176, 0.443, 0.6)
    glRectf(body_x - 0.06, body_y + 0.1, body_x + 0.06, body_y + 0.12)

    glColor3f(0.176, 0.443, 0.6)
    glRectf(body_x - 0.1, body_y + 0.33, body_x + 0.1, body_y + 0.12)


def draw_legs():
    glColor3f(0.176, 0.443, 0.6)
    glRectf(body_x - 0.1, body_y - 0.5, body_x - 0.2, body_y - 0.9)

    glColor3f(0.176, 0.443, 0.6)
    glRectf(body_x + 0.1, body_y - 0.5, body_x + 0.2, body_y - 0.9)


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    aspect_ratio = window_width / window_height
    if aspect_ratio > 1:
        glOrtho(-1 * aspect_ratio, 1 * aspect_ratio, -1, 1, -1, 1)
    else:
        glOrtho(-1, 1, -1 / aspect_ratio, 1 / aspect_ratio, -1, 1)

    glMatrixMode(GL_MODELVIEW)

    draw_upper_body()
    draw_head()
    draw_legs()

    # Moving arms up and down
    glPushMatrix()
    glRotatef(rotation_angle, 0, 0, 1)
    draw_right_arm()
    draw_left_arm()
    glPopMatrix()

    # Moving robot left and right
    glPushMatrix()
    glTranslatef(body_x, body_y, 0)
    glPopMatrix()

    # Moving legs to make the impression of walking
    glPushMatrix()
    glRotatef(rotation_angle, 0, 0, 1)
    # draw_legs()
    glPopMatrix()

    glutSwapBuffers()


def keyboard(key, x, y):
    global rotation_angle
    global body_x
    if key == b" ":
        rotation_angle = 0.0
    elif key == GLUT_KEY_UP:
        rotation_angle -= rotation_increment
    elif key == GLUT_KEY_DOWN:
        rotation_angle += rotation_increment
    elif key == GLUT_KEY_LEFT:
        body_x -= 0.05
    elif key == GLUT_KEY_RIGHT:
        body_x += 0.05

    glutPostRedisplay()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow("2D Robot Drawing")

    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutSpecialFunc(keyboard)
    glutMainLoop()


if __name__ == "__main__":
    main()
