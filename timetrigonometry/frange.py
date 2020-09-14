

def frange(start, *args, count=None):
    """
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
    """
    start, stop = (float(start), float(args[0])) if args else (0.0, float(start))
    span = stop - start
    if count is None and len(args) <= 3:
        step = float(args[1]) if len(args) == 2 else 1.0
        count = max(0, int(span / step))
        span = step * count
    elif count is not None and len(args) <= 2:
        step = None
    else:
        raise ValueError("frange takes up to 3 arguments, either 3 or 2 plus a named count, arguments")
    for i in range(count):
        yield start + span * i / count

