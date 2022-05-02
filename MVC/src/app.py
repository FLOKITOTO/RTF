from flask import Flask, render_template
from flask_migrate import Migrate

from models.plane import db
from routes.plane_bp import plane_bp

app = Flask(__name__)

app.config.from_object('config')

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(plane_bp, url_prefix='/users')

@app.route('/')

def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()