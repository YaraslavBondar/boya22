from flask import Blueprint

dynamic_inputs = Blueprint(
    'dynamic_inputs',
    __name__,
    template_folder='templates',
    url_prefix='/dynamic-inputs'
)

@dynamic_inputs.route('/main/')
def main():
    return '<h2>Hello from dynamic-inputs blueprint!</h2>'