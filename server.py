#!/usr/bin/env python2 -i
from bottle import Bottle, run, app
from bottle.ext import sqlalchemy
from bottle.ext import beaker
from bottle_log import LoggingPlugin

from models import DBBase
from routes import AllRoutes

rootApp = Bottle()

logging_opts = {
    'logging.level': 'debug',
    'logging.format': '%(asctime)s : %(levelname)s : %(filename)s.%(funcName):%(lineno)d : %(message)s'
}
rootApp.install(LoggingPlugin(logging_opts))

plugin = sqlalchemy.Plugin(
    DBBase.engine,
    DBBase.Base.metadata
)
rootApp.install(plugin)

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}
app = beaker.middleware.SessionMiddleware(rootApp, session_opts)

AllRoutes.setupRoutes(rootApp)

if __name__ == '__main__':
    run(app=app, host='localhost', port=8090, debug=True)
