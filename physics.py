import math 

# physics.py

from values import g, m

def initialize_state():
    """
    Initial state of the droplet.
    y: vertical position in pixels for now (we'll switch to meters later)
    v: vertical velocity (pixels/s-ish)
    m: mass of the droplet (kg) from values.py
    """
    return {
        "y": 300.0,   # start near the top of the window
        "v": 0.0,     # initial velocity
        "m": m,       # real mass from values.py (doesn't affect pure gravity yet)
    }

def apply_forces(state, dt):
    """
    Apply gravity to update velocity and position.

    Physically: a = g.
    Here: v = v + g * dt
          y = y + v * dt * scale
    """

    # acceleration due to gravity (independent of mass in this case)
    a = g

    # update velocity
    state["v"] += a * dt

    # update position (scaled so it looks nice on screen)
    state["y"] += state["v"] * dt * 60

    # simple floor so droplet doesn't fall off the window
    if state["y"] > 580:
        state["y"] = 580
        state["v"] = 0.0
