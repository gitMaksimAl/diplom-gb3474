from django.contrib import admin

from .models import (
    User,
    Project,
    Skill,
    Certificate,
    SocialMedia
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': [('user_name', 'email', 'active')]
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
    ordering = ('active', 'name')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': [('name', 'status')]
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
                'fields': [('publisher', 'title')]
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
    ordering = ('status',)


admin.register(SocialMedia)
admin.register(Skill)
