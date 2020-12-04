from django.contrib import admin
from complaints.models import Complain, complain_type

admin.site.register(Complain)
admin.site.register(complain_type)