from django.forms import Form, CharField


class DynamicInputs(Form):

    name = CharField()

    extra_for = 'name'
    extra_type = CharField

    def __init__(self, *args, add_new_input=False, **kwargs):
        super().__init__(*args, **kwargs)
        self._process_extra_fields(*args)
        if add_new_input:
            self._add_extra_field()

    def _get_count_fields(self, name: str) -> int:
        return sum(1 for k, _ in self.fields.items() if name in k)

    def _process_extra_fields(self, *args):
        if args:
            extra_fields = {key: value
                            for key, value in args[0].items()
                            if self.extra_for in key}
            for name, value in extra_fields.items():
                self.fields[name] = self.extra_type(
                    initial=value,
                    required=False,
                )

    def _add_extra_field(self):
        count = self._get_count_fields(self.extra_for)
        new_field_name = self.extra_for + str(count + 1)
        self.fields[new_field_name] = self.extra_type(required=False)
