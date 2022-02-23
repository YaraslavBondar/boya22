from django.forms import Form, CharField


class DynamicInputs(Form):

    name = CharField()
