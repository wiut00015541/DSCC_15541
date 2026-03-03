from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("register/", views.register, name="register"),
    path(
        "login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("create/", views.create_task, name="create_task"),
    path("update/<int:pk>/", views.update_task, name="update_task"),
    path("delete/<int:pk>/", views.delete_task, name="delete_task"),
    path(
        "status/<int:pk>/<str:new_status>/", views.change_status, name="change_status"
    ),
]
