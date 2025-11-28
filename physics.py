import math 

# physics.py

from values import g

def initialize_state():
   
    """
    Initial state of the droplet.
    y: vertical position in pixels for now (we'll switch to meters later)
    v: vertical velocity (pixels/s-ish)
    m: mass of the droplet (kg) from values.py
    """

    return {
        "x": 100.0,   # initial x position of dropplet
        "y": 300.0,   # initial y position of dropplet
        
        "vx": 7.0,    # x initial velocity
        "vy": 0.0,     # y initial velocity
    }

def apply_forces(state, dt):
    
    """
    Apply gravity to update velocity and position.

    Physically: a = g.
    Here: v = v + g * dt
          y = y + v * dt * scale
    """
    # ease of variables, switch
    x = state["x"]
    vx = state["vx"]
    
    # drag constand for display purposes 
    k = .15

    # 1D acceleration due to drag
    ax = -k * vx
    
    # update the velcoity each frame
    vx += ax * dt

    # update the x position each frame
    x += vx * dt * 60

    # ease of variables, revert
    state["x"] = x
    state["vx"] = vx



    if 400 < state["x"]:

        vy = state["vy"]
        y  = state["y"]

        # gravity acceleration
        a_y = g

        # update velocity
        vy += a_y * dt

        # update position
        y += vy * dt * 60

        state["vy"] = vy
        state["y"]  = y

    '''
    # acceleration due to gravity (independent of mass in this case)
    a_y = g
    '''
    '''
    # force region
    if state["x"] > 400 and state["x"] < 770:
        state["vy"] += g * dt
        state["y"] += state["vy"] * dt * 60
    '''

    # x right boundry 
    if state["x"] > 790.0:
        state["x"] = 790.0
        state["vx"] = 0.0
        state["vy"] = 0.0

    # y bottom boundry
    if state["y"] > 590.0:
        state["y"] = 590.0
        state["vy"] = 0.0
        state["vx"] = 0.0

    '''
    if state["y"] > 580.0:
        state["y"] = 580.0
        state["vy"] = 0.0
    '''