from django.shortcuts import render
from .models import ExamResult
from users.models import Exam, Courses, CourseEnrollment
from django.forms.models import model_to_dict


# Create your views here.


def student_graph(request, class_name):
    course_instance = Courses.objects.get(course_name=class_name)
    all_exams = Exam.objects.filter(course_id=course_instance)
    exam_result_personal = []
    average = []
    exam_max = []
    exam_total = []
    for each_exam in all_exams:
        all_exam_result = ExamResult.objects.filter(examId=each_exam)
        exam_result_personal_instance = ExamResult.objects.get(examId=each_exam, userId=request.user.registered_user.id)
        exam_sum_scored = 0
        exam_total.append(each_exam.max_marks)
        max = 0
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
    print(exam_max)
    print(average)
    print(exam_total)
    print(exam_result_personal)
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
    print(all_exams)
    print(all_students)
    count1=0
    count2=0
    count3=0
    count4=0
    count5=0
    for ex in range(len(all_exams)):
        for stud in range(len(all_students)):
            if all_students_marks[ex][stud]>=0.8*all_exams[ex].max_marks:
                count5=count5+1
            elif all_students_marks[ex][stud]>=0.6*all_exams[ex].max_marks:
                count4=count4+1
            elif all_students_marks[ex][stud]>=0.4*all_exams[ex].max_marks:
                count3=count3+1
            elif all_students_marks[ex][stud]>=0.2*all_exams[ex].max_marks:
                count2=count2+1
            elif all_students_marks[ex][stud]>=0.0*all_exams[ex].max_marks:
                count1=count1+1
    count_list=[count1 ,count2, count3, count4, count5]
    context = {
        'all_students_name': all_students_name,
        'all_students_marks': all_students_marks,
        'all_exams': all_exams,
        'class_name': class_name,
        'count_list':count_list
    }
    print(context['all_students_marks'])
    print(context['all_students_name'])
    print(context['all_exams'])
    print(context['class_name'])
    print(context['count_list'])
    return render(request, 'report/faculty_graph.html', context)
