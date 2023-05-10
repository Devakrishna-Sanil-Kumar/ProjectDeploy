from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from first_app.models import Program, Student

from .forms import StudentForm

clicked = 0
 
def index(request) :    # 'request' name is convention. It can be some other name too.
    global clicked
    program_values = Program.objects.all()
    student_values = Student.objects.all()
    my_dict = {
        'count' : clicked,
        'program_rows' : program_values,
        'student_rows' : student_values,
 }
    clicked += 1
    #my_dict = {'count' : clicked}
    #my_dict = { 'message' : "This is an injected content"}
    return render(request, 'index.html', my_dict) #HttpResponse("<h1>Hello World</h1>")

def get_student(request):    
  if request.method == 'POST':          
    form = StudentForm(request.POST)     
    if form.is_valid():
        s_name = form.cleaned_data['name']
        s_roll = form.cleaned_data['roll']
        s_degree = form.cleaned_data['degree']        
        s_branch = form.cleaned_data['branch']
        s_dob = form.cleaned_data['dob']
        s_year = form.cleaned_data['year']
        print(s_name, s_roll, s_degree, s_branch, s_year, s_dob)
        p = Program(title=s_branch, branch=s_branch)
        p.save()
        s = Student(program=p, roll_number=s_roll, name=s_name, year=s_year, dob=s_dob)
        s.save()
        return HttpResponseRedirect('/student')
  else: 
      form = StudentForm()
      return render(request, 'StudentForm.html', {'form': form})

def help(request) :
    my_dict = {'help_insert' : "HELP PAGE"}
    return render(request, 'help.html', my_dict)
