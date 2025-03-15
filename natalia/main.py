# sister_mary.natalia.main.py
from _spy.vitollino.main import Cena, Elemento
from browser import timer
from math import sin, cos
import math
import time
WALL = "http://2.bp.blogspot.com/-PytfKUGuHxU/T2HYwbL3_CI/AAAAAAAABQg/mhLu8Wfn5Mk/s1600/Seamless+wall+plaster+%252811%2529.jpg"
WOOD = "https://www.publicdomainpictures.net/pictures/210000/velka/brown-wood-grain-background-1490391486LjK.jpg"
SPOT = "https://activufrj.nce.ufrj.br/studio/Suucuri/bitmap.png?disp=inline&size=G"
class Clock:
    def __init__(self):
        c = Cena(WALL)
        clock = Elemento(WOOD, x= 50, y=50, w=200, h=200, cena=c)
        self.second = Elemento(SPOT, x= 100, y=100, w=50, h=50, cena=c)
        c.vai()
        timer.set_interval(self.set_clock, 1000)
    def pointer(self, angle):
        width = height = 200
        ray, r1 = 80, 1
        """Draw a needle at specified angle in specified color.
        r1 and r2 are percentages of clock ray.
        """
        x1 = width / 2 - ray * cos(angle) * r1
        y1 = height / 2 - ray * sin(angle) * r1
        self.second.x, self.second.y = x1, y1
    def datetime(self):
        def needle(a,b,c):
            pass
        # print day
        now_time = time.time()
        now = time.localtime(now_time)
        microsecs = now_time - int(now_time)
        day = now.tm_mday
        hour = now.tm_hour % 12 + now.tm_min / 60
        angle = hour * 2 * math.pi / 12 - math.pi / 2
        needle(angle, 0.05, 0.45)
        minute = now.tm_min
        angle = minute * 2 *math.pi / 60 - math.pi / 2
        needle(angle, 0.05, 0.7)
        ctx.lineWidth = 1
        second = now.tm_sec + microsecs
        angle = second * 2 * math.pi / 60 - math.pi / 2
        needle(angle, 0.05, 0.8)
        self.pointer(angle)
    def set_clock(self):
        self.datetime()

Clock()