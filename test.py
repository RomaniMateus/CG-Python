from OpenGL.GL import *
from OpenGL.GLUT import *
import math


def draw_circle():
    glClear(GL_COLOR_BUFFER_BIT)

    # Set the color for the circle
    glColor3f(0.0, 0.0, 1.0)  # Blue color

    # Define the circle's center and radius
    center_x, center_y = 0.0, 0.0
    radius = 0.5
    num_segments = 100  # Number of line segments to approximate the circle

    # Draw the circle using line segments
    glBegin(GL_POLYGON)
    for i in range(num_segments):
        theta = 2.0 * math.pi * i / num_segments
        x = center_x + radius * math.cos(theta)
        y = center_y + radius * math.sin(theta)
        glVertex2f(x, y)
    glEnd()

    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Circle Drawing")

    glutDisplayFunc(draw_circle)
    glutMainLoop()


if __name__ == "__main__":
    main()
