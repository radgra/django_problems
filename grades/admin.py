from django.contrib import admin
from . import models
from users.models import CustomUser
from .forms import GradeForm
# Register your models here.
@admin.register(models.Grade)

class GradeAdmin(admin.ModelAdmin):
    form = GradeForm
    list_display = ('__str__','student','subject','value') 
    def get_queryset(self,request):
        qs = super().get_queryset(request)
        user = request.user
        if user.is_superuser:
            return qs
        elif user.is_teacher:
            return qs.filter(subject__teacher=user)
        else:
            return qs.filter(student=user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'student':
            kwargs['queryset'] = CustomUser.objects.filter(is_teacher=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_form(self, request, obj=None, change=False, **kwargs):
        form_class =  super().get_form(request, obj=obj, change=change, **kwargs)
        form_class.request = request
        return form_class  
    


@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name','teacher')
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            kwargs["queryset"] = CustomUser.objects.filter(is_teacher=True)
        fm = super().formfield_for_foreignkey(db_field, request, **kwargs)
        return fm



