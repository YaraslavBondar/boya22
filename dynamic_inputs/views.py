from flask import redirect, render_template, request, url_for
from dynamic_inputs import dynamic_inputs
from dynamic_inputs.forms import DynamicForm


@dynamic_inputs.route('/main/')
def main():
    return render_template('dynamic_inputs/base.jinja')


@dynamic_inputs.route('/add/', methods=['GET', 'POST'])
def add():
    template = 'dynamic_inputs/add.jinja'
    form = DynamicForm()
    if form.validate_on_submit():
        print(form.data)
        return redirect(url_for('dynamic_inputs.add'))
    return render_template(template, form=form)
