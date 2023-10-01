# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_minify  import Minify
#from flask_migrate import Migrate

from apps import app

#Migrate(app, db)

DEBUG = app.config['DEBUG'] 

if not DEBUG:
    Minify(app=app, html=True, js=False, cssless=False)

app.logger.info('DEBUG            = ' + str( DEBUG )                 )
app.logger.info('Page Compression = ' + 'FALSE' if DEBUG else 'TRUE' )
app.logger.info('ASSETS_ROOT      = ' + app.config['ASSETS_ROOT']    )

if __name__ == "__main__":
    app.run()
