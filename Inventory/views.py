from django.views import View
from django.shortcuts import render ,redirect
from .models import *
from .urls import *

# Create your views here.
def StudentsDetail(request):
    return render(request,'stud_det.html')
    
class StudentsListView(View):

    login_url = '/'

    def get(self, request):

        context = {
        "student_data": Students_data.objects.all()
        }

        return render(request, 'stud_det.html', context)
    
class StudentsAddView( View):

    login_url = '/'

    def get(self, request):

        context = {
            'student_data': Students_data()
        }

        return render(request, 'signup.html', context)
    
    def post(self, request):

        student_data = Students_data(request.POST, request.FILES)

        if student_data.is_valid():

            student_data.save()

            return redirect('/inventory/student_list/')
    
    
