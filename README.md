# BOIDS Implementation in Python

This project implements a basic flocking simulation using BOIDS (Bird-Object-Identification-Simulation) in Python. The simulation is created using the `pyglet` and `pymunk` libraries for visual rendering and physics, respectively, while `numpy` is used for mathematical calculations. The goal is to simulate flocking behavior using three main rules: alignment, cohesion, and interaction, while ensuring that the boids remain on the screen.

## Key Features

- **Velocity Control**: Each boid has a set velocity defined by the `velocidad` variable, which dictates the speed of movement.
- **Detection Radius**: The boids are only influenced by others within a certain radius, specified by the `radio` variable.
- **Customizable Boids**: Each boid is represented by a triangular shape, with physics defined using the `pymunk` library, allowing for easy customization of their behavior and interactions.

## Auxiliary Functions

- **Distance Calculation**: The `distancia` function calculates the Euclidean distance between two points.
- **Unit Vector**: The `vector_unitario` function normalizes vectors to ensure uniform velocity, scaling them by the desired speed.

## BOID Class

Each boid is an instance of the `boid` class, which handles movement and interaction with the flock. The key methods include:

### `alinear(self, flock)`
This method aligns a boid's velocity with the average velocity of nearby boids within its detection radius. It helps to ensure that boids in proximity move in similar directions.

### `cohesionar(self, flock)`
This method makes each boid move towards the average position of nearby boids, ensuring that they stay together as a flock.

### `interactuar(self, flock)`
Combines alignment and cohesion behaviors to adjust the boid's velocity according to the forces from nearby boids. The resulting velocity is scaled using `vector_unitario` to maintain a consistent speed.

### `pantalla(self)`
Ensures that boids stay within the window bounds, wrapping them to the opposite edge when they move off-screen.

## Flock Creation

The simulation can generate a flock of boids using the `flock_creator` function. Each boid is initialized with a random velocity and position within the window space.

## Main Loop

The program runs using `pyglet`'s event-driven loop. During each frame:

1. **Window Clearing**: The screen is cleared and redrawn using `pymunk`'s debug draw.
2. **Boid Updates**: Each boid’s position and angle are updated based on its velocity, while interaction with the flock is calculated.

## Running the Simulation

To start the simulation, the program is executed in the main loop using `pyglet.app.run()` and the `update` function ensures the space is updated at regular intervals.

```python
if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1.0/60.0)
    pyglet.app.run()
## Requirements
```
To run this project, you'll need the following dependencies:

- **Python 3.x**: Make sure you have Python 3 installed on your system.
- **pyglet**: For handling the window and rendering the boids. Install it via:
  ```bash
  pip install pyglet
