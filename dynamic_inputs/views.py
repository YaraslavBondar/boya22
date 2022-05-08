from dynamic_inputs import dynamic_inputs


@dynamic_inputs.route('/main/')
def main():
    return '<h2>Hello from dynamic-inputs blueprint!</h2>'


@dynamic_inputs.route('/test/')
def test():
    return '<h2>Hello from dynamic-inputs blueprint test page!</h2>'
