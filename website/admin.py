from django.apps import apps
from django.contrib import admin
from website.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_login')


admin.site.register(User, UserAdmin)

models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
