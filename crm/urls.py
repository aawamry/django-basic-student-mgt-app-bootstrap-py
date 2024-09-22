from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index, name='index'),
    path('<int:id>', views.view_student, name='view_student'),
    path("add/", views.add, name='add'),
    path("edit/<int:id>", views.Edit, name='edit'),
    path("delete/<int:id>", views.Delete, name='delete'),
]