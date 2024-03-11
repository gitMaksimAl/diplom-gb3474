from django.contrib import admin

from .models import (
    User,
    Project,
    Skill,
    Certificate,
    SocialMedia,
    Contact
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': [('user_name', 'email', 'spec', 'active')]
            },
        ),
        (
            'detail',
            {
                'classes': ['collapse'],
                'fields': [('first_name', 'last_name', 'time_zone', 'biography')]
            }
        )
    ]
    ordering = ('active', 'user_name')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': [('user_id', 'name', 'status')]
            },
        ),
        (
            'detail',
            {
                'classes': ['collapse'],
                'fields': [('task', 'description', 'link', 'role')]
            }
        )
    ]
    ordering = ('status',)


@admin.register(Certificate)
class ProjectAdmin(admin.ModelAdmin):

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': [('user_id', 'publisher', 'title')]
            },
        ),
        (
            'detail',
            {
                'classes': ['collapse'],
                'fields': [('date', 'link')]
            }
        )
    ]
    ordering = ('publisher',)


admin.site.register(SocialMedia)
admin.site.register(Skill)
admin.site.register(Contact)
