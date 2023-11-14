
from django.urls import path, include
from .views import (
    UserView
    )

urlpatterns = [
     path('',include([
        path('', UserView.as_view({
            'get': 'list',
            'post': 'create',
        })),
        path('<int:pk>/', UserView.as_view({
            'put': 'update',
            'delete': 'destroy',
        })),
    ])),
]
