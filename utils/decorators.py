def add_get_methods(**kwargs):
    field_prefix = kwargs.get('field_prefix', '')

    def decorator(cls):
        fields = {name: value for name, value in cls.__dict__.items() if field_prefix in name}
        for name, value in fields.items():
            setattr(
                cls,
                f'''get_{name.replace(field_prefix, '').lower()}''',
                classmethod(lambda _, value=value: cls.objects.get(pk=value)),
            )
        return cls

    return decorator
