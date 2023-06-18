from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Profile, Task

admin.site.unregister(Group)
admin.site.register(Task)

# Combine profile to user
class ProfileInline(admin.StackedInline):
    model = Profile
    

# Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username','first_name','last_name','password','email']
    inlines = [ProfileInline]


# Unregister Initial User
admin.site.unregister(User)

# Register user and profile
admin.site.register(User, UserAdmin)