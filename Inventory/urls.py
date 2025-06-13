from django.contrib import admin 
from django.urls import path ,include
from .views import *

urlpatterns = [
    path('students_detail/', StudentsDetail),
    path('student_list/',StudentsListView.as_view() ),
    path('student/add_data/',StudentsAddView.as_view()),
    path('student/delete/<int:id>/', StudentDataDelete.as_view(),name='student_delete'),
    path('student/update/<int:id>/', StudentDataUpdate.as_view(),name='student_update'),
]
