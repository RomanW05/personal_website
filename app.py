import os
from flask import Flask

from routes.cache_file import cache
from routes.personal import personal
from routes.gaming import gaming
from routes.tools import tools


app = Flask(__name__)
cache.init_app(app)


# Add routes
app.register_blueprint(personal)
app.register_blueprint(gaming)
app.register_blueprint(tools)


# Initiate
if __name__ == "__main__":
    if 'personal_website' in os.path.dirname(os.path.abspath(__file__)):
        app.run(host="localhost", port=8080, debug=True)
    else:
        from waitress import serve
        serve(app, host="0.0.0.0", port=8080, threaded=True)