#!/usr/bin/env python
# coding: utf-8

import sys
import numbers
from functools import wraps
from flask import abort


def check_parameter(param_name, min_value=0, max_value=sys.float_info.max):
    def _decorator(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            parameter = kwargs.get(param_name, None)
            if parameter is None:
                abort(400)
            if not isinstance(parameter, numbers.Real):
                abort(415)
            if parameter < min_value or parameter > max_value:
                abort(422)
            return func(*args, **kwargs)
        return _wrapper
    return _decorator
