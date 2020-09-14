
from __future__ import unicode_literals
from __future__ import print_function

import os, sys


def parseargv_help(exitcode=None):
    print(__doc__)
    if exitcode is not None:
        exit(exitcode)


def parseargv(argv=none, start=0, stop=None, lstrip=''):
    if argv is None:
        argv = sys.argv
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
