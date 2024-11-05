
# admin.py
from django.contrib import admin
from .models import UserProfile,UserMessage,MedicalPurpose,FoodPurpose,ImmediatePurpose,FailMsg

admin.site.register(UserProfile)
admin.site.register(UserMessage)
admin.site.register(MedicalPurpose)
admin.site.register(FoodPurpose)
admin.site.register(ImmediatePurpose)
admin.site.register(FailMsg)