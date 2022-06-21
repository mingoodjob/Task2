from django.contrib import admin
from user.models import UserModel, UserProfile, Hobby
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    filter_horizontal = ('hobby',)
    verbose_name_plural = 'profile'


class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'fullname',)
    list_display_links = ('username', )
    list_filter = ('username', )
    search_fields = ('username', 'fullname',)

    fieldsets = (
        ("정보", {'fields': ('username', 'password', 'fullname', 'join_date',)}),
        ('권한', {'fields': ('is_admin', 'is_active', )}),)

    filter_horizontal = []

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('username', 'join_date',)
        else:
            return ('join_date', )

    inlines = [
        UserProfileInline,
        
    ]

admin.site.register(UserModel, UserAdmin)
# admin.site.register(UserProfile)
admin.site.register(Hobby)