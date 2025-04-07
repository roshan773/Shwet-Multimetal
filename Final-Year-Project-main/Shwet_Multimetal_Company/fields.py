from django.db import models
import shortuuid

class ShortUUIDField(models.CharField):
    def __init__(self, *args, **kwargs):
        # Remove unexpected keyword arguments before passing to parent class
        prefix = kwargs.pop('prefix', None)
        kwargs.setdefault('max_length', 22)  # Default length is 22 characters
        super().__init__(*args, **kwargs)
        self.prefix = prefix

    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname)
        if add and not value:
            value = shortuuid.uuid()
            if self.prefix:
                value = f"{self.prefix}-{value}"
            setattr(model_instance, self.attname, value)
        return value
