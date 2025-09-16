from django.urls import path
from . import views

urlpatterns = [
    # helloworld/
    path('home/', views.home,name='home'),
    # 13/
    path('<int:id>/<str:name>/', views.post,name='post')
]
