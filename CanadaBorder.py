import csv
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

csv_file = 'cgn_canada_csv_eng.csv'

provinces = {}
with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        province = row[11]
        if province not in provinces:
            provinces[province] = []
        provinces[province].append((float(row[8]), float(row[9])))


pygame.init()
window_size = (1440, 480)
screen = pygame.display.set_mode(window_size, GL_DOUBLEBUFFER)
glViewport(0, 0, *window_size)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, window_size[0], window_size[1], 0, -1, 1)
glMatrixMode(GL_MODELVIEW)

glClearColor(0.0, 0.0, 0.0, 0.0)
glEnable(GL_DEPTH_TEST)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT)

    for province, coords in provinces.items():
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_LINE)
        for lat, lon in coords:
            glVertex3f(lon, lat, 0.0)
        glEnd()

    pygame.display.flip()