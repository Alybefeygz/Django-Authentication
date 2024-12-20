from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser
from .forms import CustomerUserCreationForms, CustomUserChangeForm


class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomerUserCreationForms
    
    # Kullanıcı formu için hangi alanların görüntüleneceğini ayarlar
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'bio', 'location')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'bio', 'location'),
        }),
    )
    
    list_display = ('username', 'email', 'bio', 'location', 'is_staff')
    search_fields = ('username', 'email', 'bio', 'location')
    ordering = ('username',)


# Admin paneline CustomUser modelini kaydeder
admin.site.register(CustomUser, CustomUserAdmin)
