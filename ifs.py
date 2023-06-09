import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Utils import *
import numpy as np

pygame.init()

screen_width = 800
screen_height = 800
ortho_left = -500
ortho_right = 500
ortho_top = -500
ortho_bottom = 500

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Turtle Graphics')

current_position = (0, -100)
direction = np.array([0, 1, 0])

# Needed variables for lindenmmayer
axiom = 'X'
rules = {
    "F": "FF",
    "X": "F+[-F-XF-X][+FF][--XF[+X]][++F-X]"
}
draw_length = 5
angle = 10
stack = []
rule_run_number = 5

instructions = ""

points = []
x = 0
y = 0

def run_rule(run_count):
    global instructions
    instructions = axiom
    for loops in range(run_count):
        old_system = instructions
        instructions = ""
        for c in range(0, len(old_system)):
            if old_system[c] in rules:
                instructions += rules[old_system[c]]
            else:
                instructions += old_system[c]
    print("Rule")
    print(instructions)


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(ortho_left, ortho_right, ortho_top, ortho_bottom)


def line_to(x, y):
    glBegin(GL_LINE_STRIP)
    glVertex2f(current_position[0], current_position[1])
    glVertex2f(x, y)
    glEnd()

def move_to(position):
    global current_position
    current_position = (position[0], position[1])


def reset_turtle():
    global current_position
    global direction
    current_position = (0, 0)
    direction = np.array([0, 1, 0])


def draw_points():
    glBegin(GL_POINTS)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()


def draw_turtle():
    global x, y
    points.append((x, y))

    r = np.random.rand()
    if r < 0.1:
        x, y = 0.00 * x + 0.00 * y + 0.0, 0.00 * x + 0.16 * y + 0.0
    elif r < 0.86:
        x, y = 0.85 * x + 0.04 * y + 0.0, -0.04 * x + 0.85 * y + 1.6
    elif r < 0.93:
        x, y = 0.2 * x - 0.26 * y + 0.0, 0.23 * x + 0.22 * y + 1.6
    else:
        x, y = -0.15 * x + 0.28 * y + 0.0, 0.26 * x + 0.24 * y + 0.44


def draw_turtle_2():
    global x, y
    points.append((x, y))

    r = np.random.rand()
    if r < 0.33:
        x, y = 0.5 * x + 0.00 * y + 0.0, 0.00 * x + 0.5 * y + 0.5
    elif r < 0.66:
        x, y = 0.5 * x + 0.00 * y + 0.5, 0.0 * x + 0.5 * y + 0.0
    else:
        x, y = 0.5 * x - 0.0 * y + 0.0, 0.00 * x + 0.5 * y + 0.0


def forward(draw_length):
    new_x = current_position[0] + direction[0] * draw_length
    new_y = current_position[1] + direction[1] * draw_length
    line_to(new_x, new_y)


def rotate(angle):
    global direction
    direction = z_rotation(direction, math.radians(angle))

clock = pygame.time.Clock()
init_ortho()
done = False
glPointSize(1)
glColor3f(0, 1, 0)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslate(-200, -100, 0)
    glScaled(550, 550, 1)
    reset_turtle()
    draw_turtle_2()
    draw_points()
    pygame.display.flip()
    pygame.time.wait(1)
pygame.quit()

