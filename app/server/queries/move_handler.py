#!/usr/bin/env python
# coding: utf-8

from flask import Blueprint
import app.server.broadcast.move_broadcast as mv
from app.server.wrappers.get_command import get_command

move_handler = Blueprint('move_handler', __name__, url_prefix="/move")

move_commands = {'forward': mv.forward,
                 'backward': mv.backward,
                 'stop': mv.stop,
                 'left': mv.left,
                 'right': mv.right}


@move_handler.route("/", methods=['POST'])
@get_command(move_commands)
def move(command, data):
    velocity, angle = data.get('velocity', None), data.get('angle', None)
    return move_commands.get(command)(velocity=velocity, angle=angle)
