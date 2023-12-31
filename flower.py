from OpenGL.GL import *
from OpenGL.GLUT import *
import math

# Window dimensions
window_width = 800
window_height = 600

# Angle for petal rotation (initially set to 0)
rotation_angle = 0.0

# Angle increment for keyboard rotation
rotation_increment = 1.0


def draw_petals():
    global rotation_angle
    draw_circle(0.25, 0.25, 0.20, 100, 1.0, 0.0, 0.0)
    draw_circle(0.25, -0.25, 0.20, 100, 1.0, 0.0, 0.0)
    draw_circle(-0.25, 0.25, 0.20, 100, 1.0, 0.0, 0.0)
    draw_circle(-0.25, -0.25, 0.20, 100, 1.0, 0.0, 0.0)
    draw_circle(0.0, 0.35, 0.20, 100, 1.0, 0.0, 0.0)
    draw_circle(0.0, -0.35, 0.20, 100, 1.0, 0.0, 0.0)
    draw_circle(0.35, 0.0, 0.20, 100, 1.0, 0.0, 0.0)
    draw_circle(-0.35, 0.0, 0.20, 100, 1.0, 0.0, 0.0)


def draw_stalk():
    glColor3f(0.0, 1.0, 0.0)
    x_left = -0.05
    x_right = 0.05
    y_bottom = -1.0
    y_top = -0.25
    glRectf(x_left, y_bottom, x_right, y_top)


def draw_circle(c_x, c_y, rad, n, red, green, blue):
    glColor3f(red, green, blue)
    center_x, center_y = c_x, c_y
    radius = rad
    num_segments = n

    glBegin(GL_POLYGON)
    for i in range(num_segments):
        theta = 2.0 * math.pi * i / num_segments
        x = center_x + radius * math.cos(theta)
        y = center_y + radius * math.sin(theta)
        glVertex2f(x, y)
    glEnd()


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

    glPushMatrix()

    glRotatef(rotation_angle, 0, 0, 1)
    draw_petals()

    glPopMatrix()

    draw_stalk()
    draw_circle(0.0, 0.0, 0.35, 100, 1.0, 1.0, 1.0)

    glutSwapBuffers()


def keyboard(key, x, y):
    global rotation_angle
    if key == b" ":
        rotation_angle = 0.0
    elif key == GLUT_KEY_RIGHT:
        rotation_angle += rotation_increment
    elif key == GLUT_KEY_LEFT:
        rotation_angle -= rotation_increment

    glutPostRedisplay()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow("Rotating Petals")

    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutSpecialFunc(keyboard)
    glutMainLoop()


if __name__ == "__main__":
    main()
