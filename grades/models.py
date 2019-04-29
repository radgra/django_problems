from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Grade(models.Model):
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    value = models.IntegerField()
    student = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.subject}-{self.student}-{self.value}'
    

class Subject(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return self.name





# 1 only teacher can mark student on certain subject 
# 2 only teacher can see all grades for his students in subject
# 3 student can see only his grades

# -------- How to do this shit ---------------------
# 1 Assign permissions on create\update - model based - student can only view
# 2 Assign permissions object based without additional libraries

# Problem - jesli nie uzywam permission a robie wszystko logika to kazdy nowy type usera trzeba do logiki dodawac:
# https://stackoverflow.com/questions/23148216/object-level-permissions-django
# Przyklad powyzej przy filtrowaniu bierze pod uwage admina - a co jesli beda dodakowi userzy ktorzy beda mieli do tego prawa
# Przy duzym projekcie to bedzie trudne do kontrolowania