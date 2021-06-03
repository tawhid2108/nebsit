from django.conf.urls import url
from django.urls import path
from . import views 
#from .views import CategoryView
from .views import  HomeViews, AboutViews, ServiceViews




urlpatterns = [
    path('', HomeViews, name="home"),
    

]    

#path('category/<str:cats>/', CategoryView, name="category"),