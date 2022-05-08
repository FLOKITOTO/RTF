from flask import Blueprint

from controllers.planeController import store, show

plane_bp = Blueprint('plane_bp', __name__)


plane_bp.route('/create', methods=['POST'])(store)
plane_bp.route('/list', methods=['GET'])(show)
