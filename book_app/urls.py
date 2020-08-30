from book_app import views
from django.urls import path


urlpatterns = [
    path('login/',views.login),
    path('reg/',views.reg),
    path('add/',views.add),
]