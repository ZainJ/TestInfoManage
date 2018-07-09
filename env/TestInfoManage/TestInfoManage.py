from flask import Flask,Blueprint
from apps.common import at as common_at
from apps.front import at as front_at
from flask_wtf import CSRFProtect
import config

def create_app():
    app=Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(common_at)
    app.register_blueprint(front_at)
    CSRFProtect(app)
    return app

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app=create_app()
    app.run(port=8000)
