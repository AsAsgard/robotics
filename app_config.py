#!/usr/bin/env python
# coding: utf-8

import logging.config


service_connect = {
    "protocol": "ipc",
    "host": "127.0.0.1",
    "port": 5474
}


# Конфигурация журналирования
LOGGING = {
    'version': 1,
    'formatters': {  # Форматирование сообщения
        'main': {
            'format': '[%(asctime)s] %(levelname)s %(module)s: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },

    'handlers': {  # Обработчики сообщений
        #'file_handler': {
        #    'class': 'logging.FileHandler',
        #    'filename': '/tmp/trading.log',
        #    'formatter': 'main',
        #},
        'streamlogger': {
            'class': 'logging.StreamHandler',
            'formatter': 'main',
        },
    },

    'loggers': {   # Логгеры
        'prod_logger': {
            'handlers': ['streamlogger'],
            'level': 'INFO',
        },
        'devel_logger': {
            'handlers': ['streamlogger'],
            'level': 'DEBUG',
        },
    },
}

logging.config.dictConfig(LOGGING)


# Базовая конфигурация
class Config(object):
    DEBUG = False
    LOGGER_NAME = 'devel_logger'


# Конфигурация выпуска
class ProductionConfig(Config):
    DEBUG = False
    LOGGER_NAME = 'prod_logger'


# Конфигурация разработки
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    LOGGER_NAME = 'devel_logger'

# Текущая конфигурация
currentConfig = DevelopmentConfig