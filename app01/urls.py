from django.urls import path
from .views import acc

urlpatterns = [
    path('', acc, name='page_acc'),
]
