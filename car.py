from OpenGL.GL import *
from OpenGL.GLUT import *
import math

# Window dimensions
window_width = 800
window_height = 600

# Car position
car_x = 0.0
car_y = 0.0

# Movement speed
move_speed = 0.01


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


def draw_car():
    # Car body (rectangle)
    glColor3f(0.0, 0.0, 1.0)  # Blue color
    glRectf(
        car_x - 0.2, car_y - 0.1, car_x + 0.2, car_y + 0.1
    )  # Left, Bottom, Right, Top

    # Car windows (rectangles)
    glColor3f(0.8, 0.8, 0.8)  # Light gray color
    glRectf(car_x - 0.15, car_y, car_x - 0.05, car_y + 0.1)  # Left window
    glRectf(car_x + 0.05, car_y, car_x + 0.15, car_y + 0.1)  # Right window

    # Car wheels (circles)
    glColor3f(0.0, 0.0, 0.0)  # Black color
    draw_circle(car_x - 0.15, car_y - 0.15, 0.05, 100, 1.0, 1.0, 1.0)  # Left wheel
    draw_circle(car_x + 0.15, car_y - 0.15, 0.05, 100, 1.0, 1.0, 1.0)  # Right wheel


def display():
    global car_x
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

    glRotatef(move_speed, 0, 0, 1)
    draw_car()

    glPopMatrix()
    glutSwapBuffers()


def keyboard(key, x, y):
    global car_x
    if key == b" ":
        car_x = 0.0
    elif key == GLUT_KEY_LEFT:
        car_x -= move_speed
    elif key == GLUT_KEY_RIGHT:
        car_x += move_speed

    glutPostRedisplay()  # Trigger a redraw


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow("2D Car Drawing")

    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutSpecialFunc(keyboard)  # Register the keyboard function for standard keys
    glutMainLoop()


if __name__ == "__main__":
    main()
