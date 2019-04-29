from django.contrib import admin
from django.contrib.auth.models import  Permission, Group

# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email','is_teacher']
    add_fieldsets = ((None,{
        'fields':('email','password1','password2','is_teacher')}),)
    fieldsets =  (
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email','is_teacher')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )

    def save_formset(self, request, form, formset, change):
        print('ole')
        super().save_formset(self, request, form, formset, change)

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        user = form.instance
        teacher = Group.objects.get(name="Teacher")
        student = Group.objects.get(name="Student")
        user.groups.clear()
        if user.is_teacher:
            user.groups.add(teacher)
            print('all')
        else:
            user.groups.add(student)
        user.save()

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        print('ole')
        return super().changeform_view(request, object_id, form_url, extra_context)

    

admin.site.register(CustomUser, CustomUserAdmin)