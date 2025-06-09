from django.contrib import admin 
from django.urls import path ,include
from .views import *

urlpatterns = [
    path('students_detail/', StudentsDetail),
    path('student_list/',StudentsListView.as_view() ),
    path('student_data/',StudentsAddView.as_view())
    
]
