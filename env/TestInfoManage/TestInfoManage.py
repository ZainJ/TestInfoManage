from flask import Flask,Blueprint
from apps.common import at as common_at
from apps.front import at as front_at
from flask_wtf import CSRFProtect
import config
from exts import db
from flask_bootstrap import Bootstrap
def create_app():
    app=Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(common_at)
    app.register_blueprint(front_at)
    db.init_app(app)
    # CSRFProtect(app)
    Bootstrap(app)
    return app



if __name__ == '__main__':
    app=create_app()
    app.run(port=8000)
