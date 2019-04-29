from django.shortcuts import render
from .models import Grade
from .serializers import GradeSerializer
# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions


class GradeList(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = (IsAuthenticated,DjangoModelPermissions)

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        if user.is_superuser:
            return qs
        elif not user.is_teacher:
            qs = qs.filter(student=user)
        else:
            qs = qs.filter(subject__teacher=user)
        return qs

class GradeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = (IsAuthenticated,)