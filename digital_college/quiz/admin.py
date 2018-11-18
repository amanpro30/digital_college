from django.contrib import admin
from .models import quiz,multiplechoice,singlechoice,answers,matching,truefalse,respo,result
# Register your models here.
admin.site.register(quiz)
admin.site.register(multiplechoice)
admin.site.register(singlechoice)
admin.site.register(answers)
admin.site.register(matching)
admin.site.register(truefalse)
admin.site.register(respo)
admin.site.register(result)