import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import csv
import threading
import sys

pygame.init()

screen_width = 1440
screen_height = 960
csv.field_size_limit(1000000)
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Graphs in PyOpenGL')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-141, -51, 41, 84)


def plot_graph():
    glBegin(GL_POINTS)
    lines = []
    my_event = threading.Event()
    with open('canada_border_Data.csv', errors='ignore') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[5] == "WKT":
                continue
            elif row[5] == "":
                continue
            else:
                line_data = str(row[5])
                line_poly_delete = line_data.split("POLYGON")
                line_first_bracket_delete = line_poly_delete[1].split("((")
                line_second_bracket_delete = line_first_bracket_delete[1].split("))")
                line_comma_separate = line_second_bracket_delete[0].split(", ")
                lines = line_comma_separate
                for l in lines:
                    coords = l.split(" ")
                    glVertex2f(float(coords[0]), float(coords[1]))

    glEnd()

done = False
init_ortho()
glPointSize(1)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plot_graph()
    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()
