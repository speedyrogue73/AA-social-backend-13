from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.forms import UserCreationForm, UserChangeForm
from .models import User
from django.utils.html import mark_safe


class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm

    def image_tag(self, obj):
        return mark_safe('<img src="{}" style="max-width:200px; max-height:200px" />'.format(obj.avatar.url))
    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_admin',
        'avatar',
    )

    list_filter = ('is_admin',)

    filter_horizontal = ()

    fieldsets = (
        (None, {
            'fields': (
                'phone_number',
                'password',
                'email',
                'first_name',
                'last_name',
                'avatar',
                'username',
                'is_active',
                'is_admin',
            )
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'phone_number',
                'username',
                'email',
                'first_name',
                'last_name',
                'password1',
                'password2',
            ),
        }),
    )


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
