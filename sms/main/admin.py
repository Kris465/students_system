from django.contrib import admin
from .models import (Grade, Course, Student, Teacher,
                     Schedule, Attendance, AboutPage, ContactPage)

admin.site.register(AboutPage)
admin.site.register(ContactPage)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Grade)
admin.site.register(Schedule)
admin.site.register(Attendance)
