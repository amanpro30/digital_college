from django.shortcuts import render
from .forms import quiz_detail_form,single_correct_form,multi_correct_form,truefalse_form,matching_form,response_form
from .models import quiz as qz,singlechoice,multiplechoice,matching,truefalse,answers,respo,result
from datetime import datetime
from django.contrib.auth.models import User
import pytz
from users.models import Courses,Registered_College,Registered_User
from django.shortcuts import redirect
from django.http import HttpResponse
from django.forms import formset_factory
from django.contrib.auth.models import User



single_correct_FormSet=formset_factory(single_correct_form)
multi_correct_FormSet=formset_factory(multi_correct_form)
truefalse_FormSet=formset_factory(truefalse_form)
matching_FormSet=formset_factory(matching_form)


def take_quiz(request,class_name,quiz_name):
    college_name=request.user.registered_user.college_id
    college_instance=Registered_College.objects.get(Name_Of_College=college_name)
    course_instance=Courses.objects.get(course_name=class_name)
    quiz_instance = qz.objects.get(name_of_quiz=quiz_name)
    questions=singlechoice.objects.filter(college_id=college_instance,class_id=course_instance,quiz_id=quiz_instance)
    response_FormSet=formset_factory(response_form,extra=questions.count())
    if request.method=="POST":
        response_sets=response_FormSet(request.POST)
        if response_sets.is_valid():
            i=0
            for each_respo in response_sets:
                question_instance=singlechoice.objects.get(question=questions[i].question)
                selected_option=each_respo.cleaned_data.get('selected_option')
                respo_instance=respo(selected_option=selected_option,question_id=question_instance,quiz_id=quiz_instance)
                respo_instance.save()
                i=i+1
            return redirect('after:classroom:quiz:quiz_result',quiz_name=quiz_instance.name_of_quiz,class_name=course_instance)
    else:    
        response_sets=response_FormSet()
    def is_started(quiz):
        present=datetime.utcnow()
        present = pytz.utc.localize(present)
        return quiz.start_time < present
    def is_finished(quiz):
        present=datetime.utcnow()
        present = pytz.utc.localize(present)
        return quiz.end_time < present
    started=is_started(quiz_instance)
    finished=is_finished(quiz_instance)
    return render(request,'quiz/take_quiz.html',{'question':questions,'respo':response_sets,'is_started':started,'is_finished':finished, 'class_name': class_name})


def create_quiz(request,class_name):
    if request.method=='POST':
        single_correct_sets = single_correct_FormSet(request.POST)
        multi_correct_sets = multi_correct_FormSet(request.POST)
        truefalse_sets = truefalse_FormSet(request.POST)
        single_correct_sets = single_correct_FormSet(request.POST)
        multi_correct_sets = multi_correct_FormSet(request.POST)
        truefalse_sets = truefalse_FormSet(request.POST)
        matching_sets = matching_FormSet(request.POST)
        course_instance=Courses.objects.get(course_name=class_name)
        college_name=request.user.registered_user.college_id
        college_instance=Registered_College.objects.get(Name_Of_College=college_name)
        if single_correct_sets.is_valid():
            for single in single_correct_sets:
                    question=single.cleaned_data.get('question')
                    option1=single.cleaned_data.get('option1')
                    option2=single.cleaned_data.get('option2')
                    option3=single.cleaned_data.get('option3')
                    option4=single.cleaned_data.get('option4')
                    answer = single.cleaned_data.get('answer')
                    marks = single.cleaned_data.get('marks')
                    quiz_instance=qz.objects.last()
                    single_instance=singlechoice(college_id=college_instance,quiz_id=quiz_instance,class_id=course_instance,question=question,option1=option1,option2=option2,option3=option3,option4=option4,answer=answer,marks=marks)
                    single_instance.save()
        course_instance = Courses.objects.get(course_name=class_name)
        return redirect('after:classroom:class_home',class_name=course_instance.course_name)
    else:
        single_correct_sets= single_correct_FormSet()
        multi_correct_sets=multi_correct_FormSet()
        truefalse_sets=truefalse_FormSet()
        matching_sets=matching_FormSet()
        return render(request,'quiz/quiz.html',{'single_choice_form':single_correct_sets,'class_name': class_name,
    'multiple_choice_form':multi_correct_sets,'truefalse_form':truefalse_sets,'matching_form':matching_sets,})



def quiz_home(request,class_name):
    username=request.user
    user_instance=User.objects.get(username=username)
    if user_instance.registered_user.role=='F':
        if request.method == 'POST':
            form1 = quiz_detail_form(request.POST)
            if form1.is_valid():
                name_of_exam = form1.cleaned_data.get('name_of_quiz')
                start_time = form1.cleaned_data.get('start_time')
                end_time = form1.cleaned_data.get('end_time')
                instructions = form1.cleaned_data.get('instructions')
                course_instance = Courses.objects.get(course_name=class_name)
                college_name = request.user.registered_user.college_id
                college_instance = Registered_College.objects.get(Name_Of_College=college_name)
                quiz_info_instance = qz(college_id=college_instance, class_id=course_instance,
                                        name_of_quiz=name_of_exam, start_time=start_time, end_time=end_time,
                                        instructions=instructions)
                quiz_info_instance.save()
                return redirect('after:classroom:quiz:create_quiz', class_name=course_instance.course_name)
        else:
            form1 = quiz_detail_form()
        return render(request, 'quiz/quiz_info.html', {'form': form1, 'class_name': class_name})
    elif user_instance.registered_user.role=='S':
        college_name=request.user.registered_user.college_id
        college_instance=Registered_College.objects.get(Name_Of_College=college_name)
        course_instance=Courses.objects.get(course_name=class_name)
        quizzes = qz.objects.filter(class_id=course_instance,college_id=college_instance)
        print(quizzes)
        return render(request,'quiz/quiz_list.html',{'quizzes':quizzes, 'class_name': class_name})

def quiz_result(request,quiz_name,class_name):
    quiz_instance = qz.objects.get(name_of_quiz=quiz_name)
    username = request.user
    user_instance = User.objects.get(username=username)
    student_instance = Registered_User.objects.get(user_id=user_instance)
    all_responses = respo.objects.filter(quiz_id=quiz_instance)
    marks=0
    total_marks=0
    for res in all_responses:
        if res.selected_option==res.question_id.answer:
           marks=marks+res.question_id.marks
        total_marks=total_marks+res.question_id.marks
    result_instance=result(quiz_id=quiz_instance,student_id=student_instance,marks_obtained=marks,total_marks=total_marks)
    result_instance.save()
    return render(request,'quiz/quiz_result.html',{'marks':marks,'total_marks':total_marks, 'class_name': class_name})




