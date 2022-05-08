from flask import Blueprint

dynamic_inputs = Blueprint(
    'dynamic_inputs',
    __name__,
    template_folder='templates',
    url_prefix='/dynamic-inputs'
)

from dynamic_inputs.views import *
