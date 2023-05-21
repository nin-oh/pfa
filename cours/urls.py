from django.urls import path
from cours.views import (
	create_cours_view,
	detail_cours_view,
)

app_name = 'cours'

urlpatterns = [
    path('create/', create_cours_view, name="create"),
    path('<slug>/', detail_cours_view, name="detail"),
 ]