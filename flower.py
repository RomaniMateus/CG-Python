from OpenGL.GL import *
from OpenGL.GLUT import *
import math

# Window dimensions
window_width = 800
window_height = 600

# Angle for petal rotation (initially set to 0)
rotation_angle = 0.0

# Angle increment for keyboard rotation
rotation_increment = 1.0  # You can adjust the rotation speed here


def draw_petals():
    global rotation_angle
    draw_circle_with_rotation(0.25, 0.25, 0.20, 100, 1.0, 0.0, 0.0, rotation_angle)
    draw_circle_with_rotation(0.25, -0.25, 0.20, 100, 1.0, 0.0, 0.0, rotation_angle)
    draw_circle_with_rotation(-0.25, 0.25, 0.20, 100, 1.0, 0.0, 0.0, rotation_angle)
    draw_circle_with_rotation(-0.25, -0.25, 0.20, 100, 1.0, 0.0, 0.0, rotation_angle)
    draw_circle_with_rotation(0.0, 0.35, 0.20, 100, 1.0, 0.0, 0.0, rotation_angle)
    draw_circle_with_rotation(0.0, -0.35, 0.20, 100, 1.0, 0.0, 0.0, rotation_angle)
    draw_circle_with_rotation(0.35, 0.0, 0.20, 100, 1.0, 0.0, 0.0, rotation_angle)
    draw_circle_with_rotation(-0.35, 0.0, 0.20, 100, 1.0, 0.0, 0.0, rotation_angle)


def draw_stalk():
    glColor3f(0.0, 1.0, 0.0)  # Set the color for the stalk (green)
    x_left = -0.05
    x_right = 0.05
    y_bottom = -1.0
    y_top = -0.25
    glRectf(x_left, y_bottom, x_right, y_top)


def draw_circle_with_rotation(c_x, c_y, rad, n, red, green, blue, angle_degrees):
    glColor3f(red, green, blue)  # Set the color for the circle
    center_x, center_y = c_x, c_y
    radius = rad
    num_segments = n

    angle_radians = math.radians(angle_degrees)  # Convert angle to radians
    rotated_x = center_x * math.cos(angle_radians) - center_y * math.sin(angle_radians)
    rotated_y = center_x * math.sin(angle_radians) + center_y * math.cos(angle_radians)

    glBegin(GL_POLYGON)  # Draw the circle using line segments with rotation
    for i in range(num_segments):
        theta = 2.0 * math.pi * i / num_segments
        x = rotated_x + radius * math.cos(theta)
        y = rotated_y + radius * math.sin(theta)
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

    draw_stalk()
    draw_petals()
    draw_circle_with_rotation(0.0, 0.0, 0.30, 100, 1.0, 1.0, 1.0, 0.0)

    glutSwapBuffers()


def keyboard(key, x, y):
    global rotation_angle
    if key == b" ":
        # Reset rotation when spacebar is pressed
        rotation_angle = 0.0
    elif key == GLUT_KEY_RIGHT:
        # Rotate petals to the right when the right arrow key is pressed
        rotation_angle += rotation_increment
    elif key == GLUT_KEY_LEFT:
        # Rotate petals to the left when the left arrow key is pressed
        rotation_angle -= rotation_increment

    glutPostRedisplay()  # Trigger a redraw


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow("Rotating Petals")

    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutSpecialFunc(keyboard)  # Register the keyboard function for special keys
    glutMainLoop()


if __name__ == "__main__":
    main()
