#!/usr/bin/env python
# coding: utf-8

import zmq
from app_config import service_connect
from robot_config import robot_connect


def connect_robot():
    context = zmq.Context()
    sender = context.socket(zmq.PUSH)
    sender.connect(f"{service_connect.get('protocol')}://{robot_connect.get('host')}:{robot_connect.get('port')}")
    receiver = context.socket(zmq.PULL)
    receiver.bind(f"{service_connect.get('protocol')}://{service_connect.get('host')}:{service_connect.get('port')}")