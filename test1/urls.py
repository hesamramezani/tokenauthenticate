from django.urls import path
from .views import test , create , personal

urlpatterns = [

    path("test/" , test.as_view() , name = "test") ,
    path("create/" , create.as_view() , name = "create") ,
    path("personal/<int:pk>/" , personal.as_view() , name = "personal") ,

]

