from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import ProfileUser 
# Register your models here.

from django.contrib.auth.models import User
#admin.site.register(ProfileUser)

@admin.register(ProfileUser)
class ProfileAdmin(admin.ModelAdmin):

    list_display=('pk','user','phone','website','picture')
    list_display_links=('pk','user')
    list_editable=('website','picture')

    search_fields=(
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone'
    )

    list_filter=(
        'created',
        'modified',
        'user__is_active',
        'user__is_staff'
    )

    fieldsets=(
        ('Profile User',{
            'fields':(
                ('user','picture'),
                
            )
        }),
        ('Extra Info',{
            'fields':(
                ('website','phone'),
                ('biography')            
            )
        }),
        ('Metadata',{
            'fields':(
                ('created','modified'),
            )
        })
    )

    readonly_fields=('created','modified')

class ProfileUserInline(admin.StackedInline):
    #Profile in line with User
    model = ProfileUser
    can_delete=False
    verbose_name_plural= 'profiles'

class UserAdmin(BaseUserAdmin):
    #Apply Profile User in line

    inlines = (ProfileUserInline,)
    list_display=(
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User,UserAdmin)

