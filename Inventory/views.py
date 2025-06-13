from django.views import View
from django.shortcuts import render ,redirect
from .models import *
from .forms import *
from .urls import *
from django.contrib.auth.decorators import login_required



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
    
class StudentsAddView(View):

    # login_url='/'

    def get(self, request):

        context={
            'student_form':Student_Form()
        }
        return render(request, 'det_add.html', context)
    
    def post(self, request):
        context={
            'student_form':Student_Form()
        }
        new_stud_data = Student_Form(request.POST, request.FILES)
        
        # new_user = User(full_name = request.POST['name'],username = request.POST['username'], reg_no = request.POST['reg_no'], course = request.POST['course'], year = request.POST['year'], gpa = request.POST['gpa'], gmail_id = request.POST['email'], photo = request.POST['profile_photo'])

        # new_user.set_password(request.POST['password'])

        # new_user.save()

        if new_stud_data.is_valid():

            # new_user = User(full_name = request.POST['name'],username = request.POST['username'], reg_no = request.POST['reg_no'], course = request.POST['course'], year = request.POST['year'], gpa = request.POST['gpa'], gmail_id = request.POST['email'], photo = request.POST['profile_photo'])
            new_stud_data.save()

            return redirect('/inventory/student_list/')
        
        return render(request, 'det_add.html', context)
    
class StudentDataDelete(View):

    # login_url = '/'

    def get(self, request, id):

        selected_product = Students_data.objects.get(id = id)

        selected_product.delete()

        return redirect('/inventory/student_list/')
    

class StudentDataUpdate( View):

    login_url = '/'

    def get(self, request, id):

        selected_product = Students_data.objects.get(id = id)

        context = {
            "student_form" : Student_Form(instance=selected_product)
        }

        return render(request, 'det_add.html', context)

    def post(self, request, id):

        selected_product = Students_data.objects.get(id = id)

        student_form = Student_Form(request.POST, instance=selected_product)

        if student_form.is_valid():

            student_form.save()

            return redirect('/inventory/student_list/')