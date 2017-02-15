from django.contrib import admin

# Register your models here.
from member.models import MyUser

class MyUserAdmin(admin.ModelAdmin):
    list_display = ('username','follower',)


admin.site.register(MyUser, MyUserAdmin)