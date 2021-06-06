from django.conf.urls import url
from django.urls import path
from . import views 
#from .views import CategoryView
from .views import  HomeViews, ThanksViews




urlpatterns = [
    path('', HomeViews, name="home"),
    path('ThanksViews/', ThanksViews, name="thank-u"),

]    

#path('category/<str:cats>/', CategoryView, name="category"),