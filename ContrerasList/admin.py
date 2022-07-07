from django.contrib import admin
from .models import Applicant, School, Admin

admin.site.register(Applicant)
admin.site.register(School)
admin.site.register(Admin)
