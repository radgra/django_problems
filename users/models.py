from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150)
    email = models.EmailField("Email", unique=True,
                              help_text="This is our email")
    is_teacher = models.BooleanField('Teacher', default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    def save(self, *args, **kwargs):
        print('ole')
        # permission = Permission.objects.get(name__icontains="can add grade")
        super().save(*args, **kwargs)
        # if self.is_teacher:
        #     self.user_permissions.add(permission)


# @receiver(post_save, sender=CustomUser)
# def permission_handler(sender, instance, **kwargs):
#     teacher = Group.objects.get(name="Teacher")
#     student = Group.objects.get(name="Student")
#     instance.groups.clear()
#     if instance.is_teacher:
#         instance.groups.add(teacher)
#         print('all')
#     else:
#         instance.groups.add(student)
#     instance.save()
