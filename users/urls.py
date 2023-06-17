from django.urls import path
from simplenotes.users import views


urlpatterns = [
 path('', views.home, name='home'),
 path("signup/", views.SignUp.as_view(), name="signup"),
]
