from django.contrib import admin
from .models import customUser, team_user
from teams.models import teams
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


class team_user_inline(admin.TabularInline):
    model = team_user
    extra = 1
    autocomplete_fields = ['id_team']


class teams_admin(admin.ModelAdmin):
    inlines = (team_user_inline,)
    search_fields = 'name_team',
    ordering = ['name_team']

    list_display = ('name_team',)
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True


class team_user_admin(admin.ModelAdmin):
    readonly_fields = ('date_time',)

class UserAdminConfig(UserAdmin):
    inlines = [team_user_inline, ]
    model = customUser
    search_fields = ('email', 'user_name', 'first_name', 'identification')
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff', 'identification')
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'first_name',
                    'is_active', 'is_staff')
    fieldsets = (
        ('General Information', {'fields': ('email', 'user_name', 'first_name', 'identification')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'user_permissions')}),
        ('Description', {'fields': ('about',)}),
    )
    formfield_overrides = {
        customUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
        customUser.user_permissions: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})}
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'user_name', 'first_name', 'password1', 'password2', 'is_active', 'is_staff',
                'user_permissions')}
         ),
    )


admin.site.register(team_user, team_user_admin)
admin.site.register(teams, teams_admin)
admin.site.register(customUser, UserAdminConfig)
