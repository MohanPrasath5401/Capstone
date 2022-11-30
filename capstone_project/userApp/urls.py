
from django.urls import path , include
from .views import Register,Signup,CreatePost,AllPost,SpecificPost,PostUpdateView,PostDeleteView
from .views import Comment

urlpatterns = [
     path('register/',Register,name='register' ),
     path('signup/',Signup,name='signup'),
     path("createpost",CreatePost,name = "createpost"),
     path("allpost",AllPost,name = "allpost"),
     path("allpost/<int:id1>/",SpecificPost,name = "sppost"),
     path("allpost/<int:id1>/comment",Comment,name = "comment"),
     path("allpost/<int:pk>/update",PostUpdateView.as_view(),name = "update"),
     path("allpost/<int:pk>/delete",PostDeleteView.as_view(),name = "delete"), 

] 