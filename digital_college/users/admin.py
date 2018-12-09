from django.contrib import admin
from .models import Registered_User, Registered_College, Courses, Clubs, CourseEnrollment, ClubEnrollment, Exam, Assignment, Content, Topics

# Register your models here.

admin.site.register(Registered_User)
admin.site.register(Registered_College)
admin.site.register(Courses)
admin.site.register(Clubs)
admin.site.register(CourseEnrollment)
admin.site.register(ClubEnrollment)
admin.site.register(Exam)
admin.site.register(Assignment)
admin.site.register(Content)
admin.site.register(Topics)