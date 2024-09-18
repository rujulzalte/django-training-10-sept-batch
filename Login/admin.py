from django.contrib import admin

# Register your models here.
from .models import User

admin.site.register(User)

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ( 'id','username', 'age', 'mobile' ,'email', 'country')
#     search_fields = ('username', 'age', 'mobile', 'email', 'country')
#     list_filter = ('age', 'country')
