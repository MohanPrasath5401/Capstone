from django.contrib import admin
from .models import Profile1,Profile3,UpdatePost

# Register your models here.
@admin.register(Profile1)
class Profile_data(admin.ModelAdmin):
    list_display = ['mobile','company_name','company_information']

@admin.register(Profile3)
class Profile2_data(admin.ModelAdmin):
    list_display = ['name','email','qualification','skills','experience']

@admin.register(UpdatePost)
class UpdatePost_data(admin.ModelAdmin):
    list_display = ['skills','experience','no_of_opening']