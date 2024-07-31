from flask import Flask
from flask_cors import CORS
from .routes.routes import routes_bp
import os

def create_app():
    app = Flask(__name__)

    if os.getenv('FLASK_ENV', 'development') == 'production':
      app.config.from_object('config.ProductionConfig')
    else:
      app.config.from_object('config.DevelopmentConfig')


    app.register_blueprint(routes_bp)

    CORS(app, resources={r"/*": {"origins": app.config['CORS_ORIGINS']}})
    print(app.config['CORS_ORIGINS'])
    return app