from django.contrib import admin

from .models import *


class MykolaAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'person_email', 'telegram_id',
        'counter_login', 'data_reg', 'lust_login'
    )


admin.site.register(Users, MykolaAdmin)
admin.site.register(Features)
