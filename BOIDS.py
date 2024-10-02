import pyglet
import numpy as np
import random
import pymunk
from pymunk.pyglet_util import DrawOptions
from math import degrees
#----------------------------------------------------------------
#Definimos variables de Control

#Rapidez de mis Boids
velocidad =140
#Radio de detección
radio = 50

#----------------------------------------------------------------
#Funciones auxiliares
def distancia(v1, v2):
    return np.sqrt(((v1[0]-v2[0])**2) + ((v1[1]-v2[1])**2))

def vector_unitario(v,k= velocidad):
    #tomamos un vector y lo hacemos de magnitud 1
    x = v[0]
    y = v[1]
    norma = np.sqrt((x**2)+(y**2))
    #y ahora podemos escalarlo por una velocidad deseada k
    return (x*k/norma, y*k/norma)

#----------------------------------------------------------------
#Constructor de los boid
class boid:
    def __init__(self, space):
        self.position = (random.uniform(0, 960), random.randint(0, 500))
        self.velocity = (0,0)
        self.acceleration = (0,0)
        self.shape = pymunk.Poly(None, ((0,0), (10,0), (5,19)))
        self.moment = pymunk.moment_for_poly(1, self.shape.get_vertices())
        self.body = pymunk.Body(1, self.moment)
        self.shape.body = self.body
        space.add(self.body, self.shape)
        self.body.position = self.position
        self.body.velocity = self.velocity


    def alinear(self, flock):
        vision = radio
        vector = (0,0)
        total = 0
        for bird in flock:
            d = distancia(bird.position, self.position)
            if (bird != self) and (d<vision):
                vector = (vector[0] + bird.body.velocity[0], vector[1] + bird.body.velocity[1])
                total +=1
            
        if total>0:
            vector = (vector[0]/total, vector[1]/total)
            vector = (-self.body.velocity[0]+ vector[0], -self.body.velocity[1]+ vector[1])
            #vector = vector_unitario(vector)
        return vector
    
    def cohesionar(self, flock):
        vision = radio
        vector = (0,0)
        total = 0
        for bird in flock:
            d = distancia(bird.position, self.position)
            if (bird != self) and (d<vision):
                vector = (vector[0] + bird.body.position[0], vector[1] + bird.body.position[1])
                total +=1
            
        if total>0:
            vector = (vector[0]/total, vector[1]/total)
            vector = (-self.body.position[0]+ vector[0], -self.body.position[1]+ vector[1])
            #vector = vector_unitario(vector)
            vector = (-self.body.velocity[0]+ vector[0], -self.body.velocity[1]+ vector[1])
        return vector
        
    def interactuar(self, flock):
        fuerza = self.alinear(flock)
        fuerza += self.cohesionar(flock)
        self.body.velocity = vector_unitario((self.body.velocity[0] + fuerza[0],self.body.velocity[1] + fuerza[1]), velocidad)
        fuerza = (0,0)

    def pantalla(self):
        #Para que siempre estén en la pantalla
        x, y = self.body.position[0], self.body.position[1]
        if x < 0:
            self.body.position = (960, self.body.position[1])
        if x>960:
            self.body.position = (1, self.body.position[1])
        if y < 0:
            self.body.position = (self.body.position[0], 500)
        if y > 500:
            self.body.position = (self.body.position[0], 0)



        



window = pyglet.window.Window()
space = pymunk.Space()
options = DrawOptions()
#----------------------------------------------------------------
#Crear Flock
flock = []

def flock_creator(N):
    while N>0:
        flock.append(boid(space))
        N-=1



flock_creator(100) 
for b in flock:
    vect = (random.uniform(-100,100), random.uniform(-100,100))
    b.body.velocity = vector_unitario(vect,velocidad)
    

@window.event
def on_draw():
    window.clear()
    space.debug_draw(options)
    for b in flock:
        b.pantalla()
        b.body.angle = np.arctan(b.body.velocity[1]/(b.body.velocity[0]+0.000000000001)) + (-b.body.velocity[0]/np.abs(b.body.velocity[0]))*np.pi/2
        b.interactuar(flock)

def update(dt):
    space.step(dt)

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1.0/60.0)
    pyglet.app.run()