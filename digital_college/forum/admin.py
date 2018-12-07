from django.contrib import admin
from .models import ClassPost, ClassImage, ClassComment, ClassLike, ClassReply
# Register your models here.

admin.site.register(ClassPost)
admin.site.register(ClassImage)
admin.site.register(ClassComment)
admin.site.register(ClassReply)
admin.site.register(ClassLike)
