from .views import *
from flask import Blueprint

bp = Blueprint('charts', __name__, url_prefix='/chart')

bp.add_url_rule('/', view_func=test_chart)