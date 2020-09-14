# py-time-trigonometry
A trigonometry module based not on pi, but on time intervals.  Plus a few helper functions.  Written in python.

## Usage
import timetrigonometry as tt

## License
GPL-3

## Help on module timetrigonometry:
```
NAME
    timetrigonometry

FUNCTIONS
    factory()
    
    frange(start, *args, count=None)
        A stable no infinite loop floating range iterator, supports step and count.
        
        Usage with no named arguments:
            frange(stop), iterates values from 0.0 to stop by 1.0;
            frange(start, stop), iterates values from start to stop by 1.0;
            frange(start, stop, step), iterates values from start to stop by step.
        Usage with a single named argument of "count":
            frange(stop, count=count), iterates count values from 0 to stop;
            frange(start, stop, count=count), iterates count values from start
                to stop.
        Note that step and count may not be used together.
        
        Arguments:
            start   (number:)   The value to start from;
            stop    (number:)   The limit to stop at;
            step    (number:)   The interval step;
            count   (number:)   The number of intervals.
    
    tatan(slope)
    
    tatan2(y, x)
    
    tcos(t, d=1.0)
    
    tellipse(radius, *targs, offset=(0.0, 0.0), count=None)
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
    
    tlerp lambda a, b, t
    
    tsin(t, d=1.0)
    
    ttan(t, d=1.0)

DATA
    halfpi = 1.5707963267948966
    inf = 1.7976931348623157e+308
    tau = 6.283185307179586
    twopi = 6.283185307179586
```
