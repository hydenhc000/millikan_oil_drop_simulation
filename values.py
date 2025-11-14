import math

# values.py

""" purpose here is to define the values used. tweak these
values as you wish and then run the simulation to see how it 
effects the movement of the oil drop. """

# default vlaues & units for q = e:

# g = gravity = 9.81 (m/s**(2))
# d = density = 886 (kg/m**(3))
# r = radius = (1 * 10**(-6)) (m)
# m = mass = (d * (4/3) * pi * r**(3)) (kg)
# e = elementary charge = (1.6 * 10**(-19)) (C)
    
# V = potintal difference = TBD (V)
# D = distance = TBD (D)
# E = electric feild = (V/D) ()





g = 9.81
d = 886 
r = (1 * 10**(-6))
m = (d * (4 / 3) * math.pi * (r**3))
e = (1.6 * 10**(-19))

V = 600
D = (5 * 10**-3)
E = (V / D)