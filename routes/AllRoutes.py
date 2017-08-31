from StaticRoutes import *

def setupRoutes(app):
    app.route('/static/<filepath:path>', 'GET', staticHandler)
