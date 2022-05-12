from flask import Flask, render_template
from flask_migrate import Migrate
from flask_cors import CORS
from models.plane import db
from routes.plane_bp import plane_bp
from config import Conf

app = Flask(__name__)
CORS(app)


app.config.from_object(Conf)

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(plane_bp, url_prefix='/plane')


@app.route('/')

def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
