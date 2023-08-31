from django.urls import path
from . import views

urlpatterns = [
    path("", views.form_emp, name="form_emp"),
    path("list/", views.list_emp, name="list_emp"),
    path("", views.form_emp, name="form_emp"),
]
