from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from users.forms import ExamForm
from .models import ExamResult
from users.models import Exam, Courses, CourseEnrollment,Registered_User
from django.forms.models import model_to_dict


# Create your views here.


def student_graph(request, class_name):
    course_instance = Courses.objects.get(course_name=class_name)
    all_exams = Exam.objects.filter(course_id=course_instance)
    exam_result_personal = []
    average = []
    exam_max = []
    exam_total = []
    max = 0
    exam_sum_scored = 0
    username=request.user
    reg_user_instance=Registered_User.objects.get(user=username)
    for each_exam in all_exams:
        all_exam_result = ExamResult.objects.filter(examId=each_exam)
        exam_result_personal_instance = ExamResult.objects.get(examId=each_exam, userId=reg_user_instance)
        exam_total.append(each_exam.max_marks)
        for ex in all_exam_result:
            exam_sum_scored = exam_sum_scored + ex.marks_obtained
            if ex.marks_obtained > max:
                max = ex.marks_obtained
        exam_max.append(max)
        average.append(exam_sum_scored / all_exam_result.count())
        exam_result_personal.append(exam_result_personal_instance.marks_obtained)
    context = {
        'exams_max': exam_max,
        'average': average,
        'exam_total': exam_total,
        'exam_result_personal': exam_result_personal,
        'exams': all_exams,
        'class_name': class_name,
    }
    return render(request, 'report/student_graph.html', context=context)


def faculty_graph(request, class_name):
    course_instance = Courses.objects.get(course_name=class_name)
    all_exams = Exam.objects.filter(course_id=course_instance)
    all_students = CourseEnrollment.objects.filter(course_id=course_instance)
    all_students_name = []
    all_students_marks = []
    for each_student in all_students:
        all_students_name.append(each_student.student_id.user.username)
    for each_exam in all_exams:
        exam_result = []
        all_exam_result = ExamResult.objects.filter(examId=each_exam)
        for ex in all_exam_result:
            exam_result.append(ex.marks_obtained)
        all_students_marks.append(exam_result)
    if request.method == 'POST':
        examform = ExamForm(request.POST, request.FILES)
        if examform.is_valid():
            exam = Exam(course_id=Courses.objects.get(course_name=class_name),
                        exam_name=examform.cleaned_data['exam_name'],
                        max_marks=examform.cleaned_data['max_marks'],
                        contribution=examform.cleaned_data['contribution'],
                        result_file=request.FILES['result_file'])
            exam.save()
            return redirect(request.META.get('HTTP_REFERER'), class_name)
    else:
        examform = ExamForm()

    context = {
        'all_students_name': all_students_name,
        'all_students_marks': all_students_marks,
        'all_exams': all_exams,
        'class_name': class_name,
        'examform': examform,
    }
    return render(request, 'report/faculty_graph.html', context)
