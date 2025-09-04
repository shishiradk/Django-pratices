from django.urls import path
from . import views

urlpatterns = [
    # helloworld/
    path('home/', views.home),
    # 13/
    path("<int:id>/", views.post)
]
