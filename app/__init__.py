#!/usr/bin/env python
# coding: utf-8

from flask import Flask
import app_config
from app.logger import Logger


def create_app():

    Logger.info('Creating app...')
    app = Flask(__name__)
    Logger.info('App created')
    Logger.info('Configurating config...')
    app.config.from_object(app_config.currentConfig)
    Logger.info('Config configured')

    import app.server.queries.move_handler as move_handler

    app.register_blueprint(move_handler.move_handler)

    Logger.info('Blueprint registered')

    return app