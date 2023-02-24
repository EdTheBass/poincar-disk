import pygame as pg

pg.init()

class Point:
    def __init__(self, window, x, y, col):
        self.window = window
        self.x = x
        self.y = y
        self.col = col

    def draw(self):
        pg.draw.line(self.window, self.col, [self.x, self.y], [self.x, self.y], 1)

    def update(self):
        return

    def __add__(self, b):
        return Point(self.window, self.x + b.x, self.y + b.y, self.col)

    def __sub__(self, b):
        return Point(self.window, self.x - b.x, self.y - b.y, self.col)

    def __mul__(self, b):
        return Point(self.window, self.x * b, self.y * b, self.col)

class Line:
    def __init__(self, window, x1, y1, x2, y2, width, col):
        self.window = window
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.width = width
        self.col = col

    def draw(self):
        pg.draw.line(self.window, self.col, [self.x1, self.y1], [self.x2, self.y2], self.width)

    def update(self):
        return

class Rect:
    def __init__(self, window, x, y, width, height, col, border=0):
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.col = col
        self.border = border

    def draw(self):
        rect = pg.Rect(self.x, self.y, self.width, self.height)
        pg.draw.line(self.window, self.col, rect, self.border)

    def update(self):
        return

class Circle:
    def __init__(self, window, x, y, radius, col, border=0):
        self.window = window
        self.x = x
        self.y = y
        self.radius = radius
        self.col = col
        self.border = border

    def draw(self):
        pg.draw.circle(self.window, self.col, [self.x, self.y], self.radius, self.border)
    
    def update(self):
        return

class Game:
    def __init__(self, width, height, title, subroutines, bg=(0,0,0)):
        self.width = width
        self.height = height
        self.title = title
        self.bg = bg
        self.screen = pg.display.set_mode((width, height))
        self.objects = []
        self.subroutines = subroutines

        pg.display.set_caption(title)

    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            self.screen.fill(self.bg)

            for obj in self.objects:
                obj.update()
                obj.draw()

            pg.display.update()
