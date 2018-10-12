from flask import Blueprint

features = Blueprint('features', __name__, static_folder='static',
                     template_folder='templates', url_prefix='/feature')
from . import views
