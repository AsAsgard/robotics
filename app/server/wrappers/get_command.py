#!/usr/bin/env python
# coding: utf-8

from functools import wraps
from flask import abort, request

def get_command(commands: dict):
    def _decorator(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            data = request.json
            path = request.path
            if not data:
                abort(400)
            command = data.get('command', None)
            if not command:
                abort(400)
            if not isinstance(command, str):
                abort(415)
            commands_dict = commands.get(path, None)
            if command not in commands_dict.keys():
                abort(422)
            return func(command=command, data=data, *args, **kwargs)
        return _wrapper
    return _decorator
