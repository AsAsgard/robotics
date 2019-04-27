#!/usr/bin/env python
# coding: utf-8

from flask_script import Manager
from app.logger import Logger
from app import create_app
from app.server.connection.robot_connection import connect_robot
from robot_config import robot_connect

app = create_app()
manager = Manager(app)


if __name__ == "__main__":
    Logger.info('Setting connection with robot')
    success = False
    for i in range(robot_connect.get("attempts")):
        Logger.info(f'Try to set connection, attempt: {i+1}')
        success = connect_robot()
        if success:
            break
    if not success:
        Logger.info('Connection has not been setted. Terminate')
        exit(0)
    Logger.info('Connection setted')

    Logger.info('Starting server')
    manager.run()