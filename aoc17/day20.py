"""Advent of Code Day 20: Particle Swarm"""
 
import helper
import numpy as np
import re

input_data = helper.read_day(20).strip().splitlines()

particles = []
for i, line in enumerate(input_data):
    vals = np.array(re.findall(r'-?[0-9]+', line), dtype=int)
    particles.append({ 'id': i, 'p': vals[:3], 'v': vals[3:6], 'a': vals[6:], 
                       'collided': False})

# Update loop
# Stopping criterion: all of the particles have velocity and acceleration
# in the same direction.
while True:
    for i, particle in enumerate(particles):
        if not particle['collided']:
            particle['v'] += particle['a']
            particle['p'] += particle['v']

    # Check collision after tick
    for i in range(len(particles)):
        for j in range(i+1, len(particles)):
            if all(particles[i]['p'] == particles[j]['p']):
                particles[i]['collided'] = True
                particles[j]['collided'] = True
    
    # Delete colliding particles
    for i, particle in enumerate(particles):
        if particle['collided']:
            particles.pop(i)

    # Get distance from origin
    #print(np.argmin([abs(particle['p']).sum() for particle in particles]))
    # Count of particles
    print("Part 2 Count:", len(particles))