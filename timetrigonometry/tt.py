
"""
TODO:
  * Make this module python2 compatible.
  * Add documentatio for tsin, tcos, ttan, tatan, tatan2.
  * Add sequence functions to apply the time trigoometry functions to
    sequence items.
  * Add file module documentation.
"""

from collections.abc import Sequence
from numbers import Number
from sys import float_info
inf, epsilon = float_info.max, float_info.epsilon
from math import sqrt, pi, cos, sin, copysign, ceil
tlerp = lambda a, b, t: a + (b-a) * t
tau = twopi = 2 * pi
halfpi = pi / 2

from .frange import frange


def tsin(t, d=1.0):
    return (abs((t*2.0-1.0)%4.0-2.0)-1.0) * d

def tcos(t, d=1.0):
    return sqrt(1 - tsin(t) ** 2) * copysign(d, 1.0-(t+0.5)%2.0)

def ttan(t, d=1.0):
    ts = tsin(t)
    return tcos(t) / ts if ts else inf

def tatan(slope):
    pass

def tatan2(y, x):
    pass

def tellipse(radius, *targs, offset=(0.0, 0.0), count=None):
    """
    Generates points for an ellipse.

    The ellipse of "radius" or (radiusx, radiusy) is created at "offset"(x, y)
    at either "count" intervals, or by step as a fourth argument if "start",
    "stop", "step" arguments are supplied.

    Arguments:
        radius (Number or (Number, Number):) the radius of the ellipse;
        start (Number:) the start time for the ellipse (default:0.0;
        stop (Number:) the stoping time for the ellipse (default 2.0);
        step (Number:) the steping for the ellipse;
        offset ((Number, Number):) a named argument offset (default (0,0)).
        count (Number:) a named argument as the number of intervals.

    Note that step and count arguments may not be used together.
    """
    if isinstance(radius, Number):
        radius = (radius, radius)
    if not isinstance(radius, Sequence) or len(radius) != 2 \
            or any(not isinstance(i, Number) for i in radius):
        raise ValueError("radius expects a number or numeric item 2-tuple")
    rx, ry = radius
    if len(targs) == 0:
        targs = (-1, 1)
    if count is None and len(targs) < 3:
        count = 2 * sqrt(rx * ry)
    tkwargs = {} if count is None else {"count": int(count)}
    if not isinstance(offset, Sequence) or len(offset) != 2 \
            or any(not isinstance(i, Number) for i in offset):
        raise ValueError("offset expects a numeric item 2-tuple")
    ox, oy = offset
    print(targs, tkwargs)
    return tuple((ox+tsin(t, rx), oy+tcos(t, ry))
                 for t in frange(*targs, **tkwargs))



