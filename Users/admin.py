from django.contrib import admin
from Users.models import *
class StudentAdmin(admin.ModelAdmin):
    list_display = ('username', 'created_on', 'last_login_on')


admin.site.register(Student, StudentAdmin)
# Register your models here.
