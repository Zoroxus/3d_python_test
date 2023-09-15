from object_3d import *
from camera import *
from projection import *
import pygame as pg


class SoftwareRender:
    def __init__(self):
        pg.init()
        self.RES=self.WIDTH,self.HEIGHT=1900,1000
        self.H_WIDTH,self.H_HEIGHT=self.WIDTH//2,self.HEIGHT//2
        self.FPS=60
        self.screen=pg.display.set_mode(self.RES)
        self.clock=pg.time.Clock()
        self.create_objects()

    def create_objects(self):
        self.camera = Camera(self,[0,1,-4])
        self.projection = Projection(self)
        self.object=Object3D(self)
        self.object.translate([0,0.5,-0.5])
        self.object.rotate_y(math.pi/6)

    def draw(self):
        self.screen.fill(pg.Color('black'))
        self.object.draw()

    def run(self):
        stateTrans = True
        while True:
            #self.object.rotate_x(math.pi/6)
            self.object.rotate_y(-math.pi/240)
            #self.object.rotate_z(math.pi/6)
            stateInt = 0
            self.object.translate([0,0.00001,0])
            self.draw()
            [exit() for i in pg.event.get() if i.type==pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)

if __name__ == '__main__':
    app=SoftwareRender()
    app.run()