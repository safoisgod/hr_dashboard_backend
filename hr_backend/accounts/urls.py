from django.contrib import admin
from django.urls import path
from .views import CreateUserView, ListUsersView, RetrieveUserView, UpdateUserView, DeleteUserView

urlpatterns = [
    path('users/', ListUsersView.as_view(), name='user-list'),
    path('users/create/', CreateUserView.as_view(), name='user-create'), 
    path('users/<int:pk>/', RetrieveUserView.as_view(), name='user-detail'),
    path('users/<int:pk>/update/', UpdateUserView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', DeleteUserView.as_view(), name='user-delete'),
]