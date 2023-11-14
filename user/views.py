from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from .forms import Create_User_Form
from rest_framework.response import Response
# Create your views here.


#User CRUD API 
class UserView(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()
    
    
