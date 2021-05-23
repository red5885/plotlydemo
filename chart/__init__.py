from .views import *
from flask import Blueprint

bp = Blueprint('charts', __name__, url_prefix='/chart')

bp.add_url_rule('/hard', view_func=test_chart)
bp.add_url_rule('/fetch', view_func=fetch_chart)
bp.add_url_rule('/data', view_func=get_data)