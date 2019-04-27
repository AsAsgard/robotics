#!/usr/bin/env python
# coding: utf-8

from app.server.wrappers.check_parameters import check_parameter
import robot_config as rc


@check_parameter(param_name="velocity", max_value=rc.maxVelocity)
def forward(velocity, *args, **kwargs):
    return "", 204


@check_parameter(param_name="velocity", max_value=rc.maxVelocity)
def backward(velocity, *args, **kwargs):
    return "", 204


def stop(*args, **kwargs):
    return "", 204


@check_parameter(param_name="angle", max_value=rc.maxAngle)
@check_parameter(param_name="velocity", max_value=rc.maxVelocity)
def left(velocity, angle, *args, **kwargs):
    return "", 204


@check_parameter(param_name="angle", max_value=rc.maxAngle)
@check_parameter(param_name="velocity", max_value=rc.maxVelocity)
def right(velocity, angle, *args, **kwargs):
    return "", 204