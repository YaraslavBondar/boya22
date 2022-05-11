import json

from flask import jsonify, redirect, render_template, url_for

from dynamic_inputs import dynamic_inputs
from dynamic_inputs.forms import DynamicForm
from dynamic_inputs.utils import (get_all_from_db, get_from_db, prepare_data,
                                  save_to_db)


@dynamic_inputs.route('/main/')
def main():
    return render_template('dynamic_inputs/base.jinja')


@dynamic_inputs.route('/add/', methods=['GET', 'POST'])
def add():
    template = 'dynamic_inputs/add.jinja'
    form = DynamicForm()
    if form.validate_on_submit():
        save_to_db(prepare_data(form.data))
        return redirect(url_for('dynamic_inputs.list'))
    return render_template(template, form=form)

@dynamic_inputs.route('/detail/<int:id>', methods=['GET'])
def detail(id):
    entry = get_from_db(id)
    return jsonify(json.loads(entry.json))


@dynamic_inputs.route('/list/', methods=['GET'])
def list():
    template = 'dynamic_inputs/list.jinja'
    entrys = get_all_from_db()
    return render_template(template, entrys=entrys)
