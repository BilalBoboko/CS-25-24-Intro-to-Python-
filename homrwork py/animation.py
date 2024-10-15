import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Вершины куба
vertices = [
    [1, 1, -1],
    [1, -1, -1],
    [-1, -1, -1],
    [-1, 1, -1],
    [1, 1, 1],
    [1, -1, 1],
    [-1, -1, 1],
    [-1, 1, 1]
]

# Ребра куба
edges = [
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 0],
    [4, 5],
    [5, 6],
    [6, 7],
    [7, 4],
    [0, 4],
    [1, 5],
    [2, 6],
    [3, 7]
]


# Функция для рисования куба
def draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


# Основная программа
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # Настройка перспективы
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)  # Перемещение куба "вглубь экрана"

    rotation_speed = [1, 1, 1]  # Скорости вращения по осям (x, y, z)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Очистка экрана и буфера глубины
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Вращение куба
        glRotatef(1, rotation_speed[0], rotation_speed[1], rotation_speed[2])

        # Рисование куба
        draw_cube()

        pygame.display.flip()
        pygame.time.wait(10)  # Задержка для плавности вращения


if __name__ == "__main__":
    main()
