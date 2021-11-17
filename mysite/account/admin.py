from django.contrib import admin
from .models import Instructor, Student, User


admin.site.register(User)
# Register your models here.
admin.site.register(Student)
# Register your models here.
admin.site.register(Instructor)
# Register your models here.


