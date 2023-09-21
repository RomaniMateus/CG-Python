from OpenGL.GL import *
from OpenGL.GLUT import *
import math

# Window dimensions
window_width = 800
window_height = 600


def draw_petals():
    draw_circle(0.35, 0.35, 0.20, 100, 1.0, 0.0, 0.0)
    draw_circle(0.35, -0.35, 0.20, 100, 1.0, 0.0, 0.0)
    draw_circle(-0.35, 0.35, 0.20, 100, 1.0, 0.0, 0.0)
    draw_circle(-0.35, -0.35, 0.20, 100, 1.0, 0.0, 0.0)
    draw_circle(0.0, 0.35, 0.20, 100, 1.0, 0.0, 0.0)
    draw_circle(0.0, -0.35, 0.20, 100, 1.0, 0.0, 0.0)
    draw_circle(0.35, 0.0, 0.20, 100, 1.0, 0.0, 0.0)
    draw_circle(-0.35, 0.0, 0.20, 100, 1.0, 0.0, 0.0)


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Set up the projection matrix
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Maintain the aspect ratio while setting up the projection matrix
    aspect_ratio = window_width / window_height
    if aspect_ratio > 1:
        glOrtho(-1 * aspect_ratio, 1 * aspect_ratio, -1, 1, -1, 1)
    else:
        glOrtho(-1, 1, -1 / aspect_ratio, 1 / aspect_ratio, -1, 1)

    glMatrixMode(GL_MODELVIEW)

    draw_petals()
    draw_circle(0.0, 0.0, 0.35, 100, 1.0, 1.0, 1.0)

    glutSwapBuffers()


def draw_circle(c_x, c_y, rad, n, red, green, blue):
    # Set the color for the circle
    glColor3f(red, green, blue)  # Blue color

    # Define the circle's center and radius
    center_x, center_y = c_x, c_y
    radius = rad
    num_segments = n  # Number of line segments to approximate the circle

    # Draw the circle using line segments
    glBegin(GL_POLYGON)
    for i in range(num_segments):
        theta = 2.0 * math.pi * i / num_segments
        x = center_x + radius * math.cos(theta)
        y = center_y + radius * math.sin(theta)
        glVertex2f(x, y)
    glEnd()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow("Perfect Circles Drawing")

    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()
