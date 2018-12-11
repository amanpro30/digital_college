from django.contrib import admin
from .models import quiz,multiplechoice,singlechoice,answers,truefalse,respo_single,respo_multiple,respo_true,result
# Register your models here.
admin.site.register(quiz)
admin.site.register(multiplechoice)
admin.site.register(singlechoice)
admin.site.register(answers)
#admin.site.register(matching)
admin.site.register(truefalse)
admin.site.register(respo_single)
admin.site.register(respo_multiple)
#admin.site.register(respo_match)
admin.site.register(respo_true)
admin.site.register(result)