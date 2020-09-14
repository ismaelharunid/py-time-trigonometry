#!/usr/bin/python
# -*- coding: latin-1 -*-

"""
ttellipse.py -- Examples by Ismael Harun (https://github.com/ismaelharunid)
An example of using timetrigonometry.py's tellipse function.
This creates an image filled with ellipses using 2 different methods. The
first type is using filled rectangles, the second filling a polygon.
See "https://github.com/ismaelharunid/py-time-trigonometry.git" for more
information on time trigonometry and timetrigonometry module.
CLI Usage:
    python ttellipse.py [options]
Options:
    -h, --help          Print this doc text.
    --show              To not show the results or to show. 
    --save[imagepath]   Save the result to imagepath (default: "".)
Notes:
  * By default the image is saved, you can disable it by using the "--save="
    without and filename.
"""

from __future__ import unicode_literals
from __future__ import print_function

import os, sys
from PIL.ImageDraw import Image, ImageDraw
import timetrigonometry as tt


def parseargv(argv, start=0, stop=None, lstrip=''):
    n_argv = len(argv)
    if stop is None:
        stop = n_argv
    args, kwargs = [], {}
    i_argv = start
    while i_argv < stop:
        arg = argv[i_argv]
        l_arg = len(arg)
        if arg[0] != '-' or l_arg < 2:
            args.append(arg)
            i_argv += 1
            continue
        if arg == "--":
            stop = i_argv
            i_argv += 1
            continue
        key, value = arg.lstrip(lstrip), ""
        if "=" in arg:
            i = arg.index("=")
            key, value = key[:i], key[i+1:]
        if key in kwargs:
            msg = "Multiple {:s} keys at {:d}" \
                    .format(repr(key), i_argv)
            if kwargs[key] or value:
                msg += ", previous '{:s}', current '{:s}'" \
                        .format(kwargs[key], value)
            raise ValueError(msg)
        kwargs[key] = value
        i_argv += 1
    return args, kwargs


def main(progname, **kwargs):
    options = {"save": "./ttellipse.png"}
    options.update(**kwargs)
    im = Image.new("RGBA", (800, 800))
    imd = ImageDraw(im)

    # background pattern
    imd.rectangle((0, 0, 800, 800), (0, 0, 255))
    for i in range(400):
        imd.polygon(tuple(tt.tellipse(9, offset=(40*(i%20+.5), 40*(i//20+.5)))),
                    (0, 255, 0)) # fill
    for i in range(441):
        imd.polygon(tuple(tt.tellipse(4.5, offset=(40*(i%21), 40*(i//21)))),
                    (255, 0, 0)) # fill

    # bigger
    xy = tuple(tt.tellipse(300, offset=(400, 400)))
    imd.polygon(xy, (255, 255, 0)) # fill
    imd.line(xy + xy[0], (255, 0, 255), 18) # stroke

    # smaller
    n_xy = 400
    xy = tuple(tt.tellipse(200, 0, 1, count=n_xy))
    x0, y0 = xy[0]
    for i_xy in range(1, n_xy):
        x1, y1 = xy[i_xy]
        a, b = (x0, x1) if x0 < x1 else (x1, x0)
        c, d = (y0, y1) if y0 < y1 else (y1, y0)
        imd.rectangle((400-a, 400+c, 400+b, 400+d), (0, 255, 255))
        x0, y0 = x1, y1

    if options["save"] and type(options["save"]) is str:
        im.save(options["save"])
        print("{:}: image written to {:s}".format(progname, options["save"]))
    if "show" in options:
        im.show()


if __name__ == "__main__":
    try:
        args, kwargs = parseargv(sys.argv, lstrip='-')
        if len(args) > 1:
            raise ValueError("unused extra arguments: {:}"
                             .format(', '.join(args)))
        for k in kwargs.keys():
            if k not in ("h", "help", "show", "save"):
                raise ValueError("unrecognized option: {:}".format(k))
    except ValueError as ve:
        print("{:}:".format(sys.argv[0]), ve)
        print("type 'python {:} --help' for usage.".format(sys.argv[0]))
        exit(-1)
    if "h" in kwargs or "help" in kwargs:
        print(__doc__)
        exit(0)
    main(*args, **kwargs)
    exit(0)

