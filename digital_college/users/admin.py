from django.contrib import admin
from .models import Registered_User, Registered_College, Courses, Clubs, CourseEnrollment, ClubEnrollment

# Register your models here.

admin.site.register(Registered_User)
admin.site.register(Registered_College)
admin.site.register(Courses)
admin.site.register(Clubs)
admin.site.register(CourseEnrollment)
admin.site.register(ClubEnrollment)