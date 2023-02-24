import game
import numpy as np

WIDTH = 500
HEIGHT = 500

D_RADIUS = 200

def circ_to_absolute(theta):
    x,y = [np.sin(theta), np.cos(theta)]
    x *= D_RADIUS
    y *= D_RADIUS
    return [WIDTH//2+x, HEIGHT//2+y]

def arc_center(p1, p2):
    x1,y1 = p1
    x2,y2 = p2
    
    x = (y1*y2*y2 - y2*x1*x1 - y2*y1*y1 + y1*x2*x2)/(y1*x2 - y2*x1)
    y = (x2*x2)/y2 - (x2/y2)*x + y2
    return [x,y]

def radius(p1, ax, ay):
    x1,y1 = p1

    return np.sqrt((x1 - ax)**2 + (y1 - ay)**2)

g = game.Game(WIDTH, HEIGHT, "Poincaré Disk", [])

disk = game.Circle(g.screen, WIDTH//2, HEIGHT//2, D_RADIUS, (255, 255, 255), border=1)

t1 = 0.5
p1_pos = circ_to_absolute(t1)
p1 = game.Point(g.screen, p1_pos[0], p1_pos[1], (255, 0, 0))

t2 = np.pi
p2_pos = circ_to_absolute(t2)
p2 = game.Point(g.screen, p2_pos[0], p2_pos[1], (0, 255, 0))

ax,ay = arc_center(p1_pos, p2_pos)
radius = radius(p1_pos, ax, ay)
arc = game.Circle(g.screen, ax, ay, radius, (0, 0, 255), border=1)

print(radius)


g.objects.append(disk)
g.objects.append(p1)
g.objects.append(p2)
g.objects.append(arc)

g.run()

