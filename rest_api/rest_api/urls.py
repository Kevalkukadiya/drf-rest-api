from django.contrib import admin
from django.urls import path
from api import views

# Function Based 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.student_api),
    path('studentapi/<int:pk>/', views.student_api),


# CLass Based
    path('classstudentapi/', views.StudentAPI.as_view()),
    path('classstudentapi/<int:pk>/', views.StudentAPI.as_view()),

#GenericAPIView and  Model Mixin CRUD
    
    path('gstudentapil/', views.StudentList.as_view()),
    path('gstudentapic/', views.StudentCreate.as_view()),
    path('gstudentapir/<int:pk>/', views.StudentRetrive.as_view()),
    path('gstudentapiu/<int:pk>/', views.StudentUpdate.as_view()),
    path('gstudentapid/<int:pk>/', views.StudentDestroy.as_view()),
    

# Generic View and Model in One

    path('gstudentapi/', views.LCStudent.as_view()),
    path('gstudentapi/<int:pk>/', views.RUDStudent.as_view()),

# List API View
    
    path('lstudentapi/', views.StudentList.as_view()),
    path('cstudentapi/', views.StudentCreate.as_view()),
    path('rstudentapi/<int:pk>/', views.StudentRetrive.as_view()),
    path('ustudentapi/<int:pk>/', views.StudentUpdate.as_view()),
    path('dstudentapi/<int:pk>/', views.StudentDelete.as_view()),
    


# List API View One

    path('lcstudentapi/', views.StudentLC.as_view()),
    path('rudstudentapi/<int:pk>/', views.StudentRUD.as_view()),

]
