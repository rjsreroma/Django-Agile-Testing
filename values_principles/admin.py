from django.contrib import admin  # type: ignore
from values_principles.models import Value, Principle

admin.site.register(Value)
admin.site.register(Principle)
