from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.

def test(request):
    return render(request,'report/test.html')
=======
from .models import ExamResult
from users.models import Exam,Courses
from django.forms.models import model_to_dict
import simplejson

# Create your views here.


def student_graph(request, class_name ):
    course_instance = Courses.objects.get(course_name=class_name)
    all_exams = Exam.objects.filter(course_id=course_instance)
    exam_results = []
    for exam in all_exams:
        exam_result_instance=ExamResult.objects.filter(examId=exam)
        exam_results.append(exam_result_instance)
    for item in all_exams:
        item['exam_name'] = model_to_dict(item['exam_name'])
    context = {
        'exams': simplejson.dumps(all_exams),
        'exam_results': exam_results
    }
    print(context['exam_results'])
    print(context['exams'])
    return render(request, 'report/student_graph.html',context=context)


def faculty_graph(request , class_name):
    return render(request, 'report/faculty_graph.html')


>>>>>>> 14f158157c979a2936952e3b943b3a4495be888c
