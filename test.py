from OpenGL.GL import *
from OpenGL.GLUT import *
import math

# Window dimensions
window_width = 800
window_height = 600

# Angle for petal rotation (initially set to 0)
rotation_angle = 0.0


def draw_petals():
    global rotation_angle  # Use the global rotation_angle variable
    draw_circle_with_rotation(0.25, 0.25, 0.20, 100, 1.0, 0.0, 0.0, rotation_angle)
    draw_circle_with_rotation(0.25, -0.25, 0.20, 100, 1.0, 0.0, 0.0, rotation_angle)
    draw_circle_with_rotation(-0.25, 0.25, 0.20, 100, 1.0, 0.0, 0.0, rotation_angle)
    draw_circle_with_rotation(-0.25, -0.25, 0.20, 100, 1.0, 0.0, 0.0, rotation_angle)
    draw_circle_with_rotation(0.0, 0.35, 0.20, 100, 1.0, 0.0, 0.0, rotation_angle)
    draw_circle_with_rotation(0.0, -0.35, 0.20, 100, 1.0, 0.0, 0.0, rotation_angle)
    draw_circle_with_rotation(0.35, 0.0, 0.20, 100, 1.0, 0.0, 0.0, rotation_angle)
    draw_circle_with_rotation(-0.35, 0.0, 0.20, 100, 1.0, 0.0, 0.0, rotation_angle)

    # Increment the rotation angle for the next frame
    rotation_angle += 1.0  # You can adjust the rotation speed here


def draw_stalk():
    # Set the color for the stalk (green)
    glColor3f(0.0, 1.0, 0.0)

    # Define the stalk's dimensions
    x_left = -0.05
    x_right = 0.05
    y_bottom = -1.0
    y_top = -0.25

    # Draw the stalk as a rectangle
    glRectf(x_left, y_bottom, x_right, y_top)


def draw_circle_with_rotation(c_x, c_y, rad, n, red, green, blue, angle_degrees):
    # Set the color for the circle
    glColor3f(red, green, blue)

    # Define the circle's center and radius
    center_x, center_y = c_x, c_y
    radius = rad
    num_segments = n  # Number of line segments to approximate the circle

    # Apply rotation to the petal positions
    angle_radians = math.radians(angle_degrees)
    rotated_x = center_x * math.cos(angle_radians) - center_y * math.sin(angle_radians)
    rotated_y = center_x * math.sin(angle_radians) + center_y * math.cos(angle_radians)

    # Draw the circle using line segments with rotation
    glBegin(GL_POLYGON)
    for i in range(num_segments):
        theta = 2.0 * math.pi * i / num_segments
        x = rotated_x + radius * math.cos(theta)
        y = rotated_y + radius * math.sin(theta)
        glVertex2f(x, y)
    glEnd()


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

    draw_stalk()
    draw_petals()
    draw_circle_with_rotation(0.0, 0.0, 0.35, 100, 1.0, 1.0, 1.0, 0.0)
    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow("Rotating Petals")

    glutDisplayFunc(display)
    glutIdleFunc(display)  # Call display function continuously
    glutMainLoop()


if __name__ == "__main__":
    main()
