from flask import Blueprint

datalattes_bp = Blueprint('datalattes_bp', __name__)

from . import views
