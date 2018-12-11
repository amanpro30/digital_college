from django.shortcuts import render
from .forms import quiz_detail_form,single_correct_form,multi_correct_form,truefalse_form,response_single_form,response_multiple_form,response_true_form,answer_form
from .models import quiz as qz,singlechoice,multiplechoice,truefalse,answers,respo_single,respo_multiple,respo_true,result
from datetime import datetime
from django.contrib.auth.models import User
import pytz
from users.models import Courses,Registered_College,Registered_User
from django.shortcuts import redirect
from django.http import HttpResponse
from django.forms import formset_factory
from django.contrib.auth.models import User
import ast

single_correct_FormSet=formset_factory(single_correct_form)
multi_correct_FormSet=formset_factory(multi_correct_form)
truefalse_FormSet=formset_factory(truefalse_form)

def take_quiz(request,class_name,quiz_name):
    college_name=request.user.registered_user.college_id
    college_instance=Registered_College.objects.get(Name_Of_College=college_name)
    course_instance=Courses.objects.get(course_name=class_name)
    quiz_instance = qz.objects.get(name_of_quiz=quiz_name)
    question_single=singlechoice.objects.filter(college_id=college_instance,class_id=course_instance,quiz_id=quiz_instance)
    question_multiple=multiplechoice.objects.filter(college_id=college_instance,class_id=course_instance,quiz_id=quiz_instance)
    question_true=truefalse.objects.filter(college_id=college_instance,class_id=course_instance,quiz_id=quiz_instance)
    response_single_FormSet=formset_factory(response_single_form,extra=question_single.count())
    response_multiple_FormSet=formset_factory(response_multiple_form,extra=question_multiple.count())
    response_true_FormSet=formset_factory(response_true_form,extra=question_true.count())
    username=request.user
    user_instance=User.objects.get(username=username)
    reg_user_instance=Registered_User.objects.get(user=user_instance)
    if request.method=="POST":
        response_single_sets=response_single_FormSet(request.POST,prefix='fs1')
        response_multiple_sets=response_multiple_FormSet(request.POST,prefix='fs2')
        response_true_sets=response_true_FormSet(request.POST,prefix='fs3')
        if response_single_sets.is_valid() and response_multiple_sets.is_valid() and response_true_sets.is_valid():
            i=0
            for (each_question,each_respo) in zip(question_single,response_single_sets):
                each_respo_instance=each_respo.save(commit=False)
                each_respo_instance.user_id=reg_user_instance
                each_respo_instance.question_id=each_question
                each_respo_instance.quiz_id=quiz_instance
                each_respo.save()
                i=i+1
            i=0
            for (each_question,each_respo) in zip(question_multiple,response_multiple_sets):
                each_respo_instance=each_respo.save(commit=False)
                each_respo_instance.user_id=reg_user_instance
                each_respo_instance.question_id=each_question
                each_respo_instance.quiz_id=quiz_instance
                each_respo.save()
                i=i+1
            i=0
            for (each_question,each_respo) in zip(question_true,response_true_sets):
                each_respo_instance=each_respo.save(commit=False)
                each_respo_instance.user_id=reg_user_instance
                each_respo_instance.question_id=each_question
                each_respo_instance.quiz_id=quiz_instance
                each_respo.save()
                i=i+1
            i=0
            return redirect('after:classroom:quiz:quiz_result',quiz_name=quiz_instance.name_of_quiz,class_name=course_instance)
    else:    
        response_single_sets=response_single_FormSet(prefix='fs1')
        response_multiple_sets=response_multiple_FormSet(prefix='fs2')
        response_true_sets=response_true_FormSet(prefix='fs3')
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
    
    context={
        'question_single':question_single,
        'question_multiple':question_multiple,
        'question_true':question_true,
        'respo_single':response_single_sets,
        'respo_multi':response_multiple_sets,
        'respo_true':response_true_sets,
        'is_started':started,
        'is_finished':finished,
        'class_name': class_name,
    }
    return render(request,'quiz/take_quiz.html',context)




def create_quiz(request,class_name):
    if request.method=='POST':
        single_correct_sets = single_correct_FormSet(request.POST,prefix='fs1')
        multi_correct_sets = multi_correct_FormSet(request.POST,prefix='fs2')
        truefalse_sets = truefalse_FormSet(request.POST,prefix='fs3')
        course_instance=Courses.objects.get(course_name=class_name)
        college_name=request.user.registered_user.college_id
        college_instance=Registered_College.objects.get(Name_Of_College=college_name)
        quiz_instance=qz.objects.last()
        print(truefalse_sets.is_valid())
        print(truefalse_sets)
        print(truefalse_sets.errors)
        if single_correct_sets.is_valid():
            for single in single_correct_sets:
                single_ins=single.save(commit=False)
                single_ins.quiz_id=quiz_instance
                single_ins.college_id=college_instance
                single_ins.class_id=course_instance
                if single.cleaned_data.get('question'):
                    single_ins.save()
        if multi_correct_sets.is_valid():
            for multiple in multi_correct_sets:
                multiple_ins=multiple.save(commit=False)
                multiple_ins.quiz_id=quiz_instance
                multiple_ins.college_id=college_instance
                multiple_ins.class_id=course_instance
                if multiple.cleaned_data.get('question'):
                    multiple_ins.save()
                    option_list=ast.literal_eval(str(multiple.cleaned_data.get('options')))
                    for j in option_list:
                        ans_ins=answers(option=j,question_id=multiple_ins)
                        ans_ins.save()
        if truefalse_sets.is_valid():
            for tf in truefalse_sets:
                print(tf)
                tf_ins=tf.save(commit=False)
                tf_ins.quiz_id=quiz_instance
                tf_ins.college_id=college_instance
                tf_ins.class_id=course_instance
                if tf.cleaned_data.get('question'):
                    tf_ins.save()
        return redirect('after:classroom:class_home',class_name=course_instance.course_name)
    else:
        single_correct_sets= single_correct_FormSet(prefix='fs1')
        multi_correct_sets=multi_correct_FormSet(prefix='fs2')
        truefalse_sets=truefalse_FormSet(prefix='fs3')
        #matching_sets=matching_FormSet(prefix='fs4')
    context={
        'class_name': class_name,
        'single_choice_form':single_correct_sets,
        'multiple_choice_form':multi_correct_sets,
        'truefalse_form':truefalse_sets,
    }
    return render(request,'quiz/quiz.html',context)




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
    reg_user_instance=Registered_User.objects.get(user=user_instance)
    student_instance = Registered_User.objects.get(user_id=user_instance)
    all_single_responses = respo_single.objects.filter(quiz_id=quiz_instance,user_id=reg_user_instance)
    all_multi_responses = respo_multiple.objects.filter(quiz_id=quiz_instance,user_id=reg_user_instance)
    all_true_responses  = respo_true.objects.filter(quiz_id=quiz_instance,user_id=reg_user_instance)
    marks=0
    total_marks=0
    for res in all_single_responses:
        if res.selected_option==res.question_id.answer:
           marks=marks+res.question_id.marks
        total_marks=total_marks+res.question_id.marks
    for res in all_true_responses:
        if res.selected_option==res.question_id.answer:
           marks=marks+res.question_id.marks
        total_marks=total_marks+res.question_id.marks
    for res in all_multi_responses:
        question_instance=res.question_id
        answer_instances=answers.objects.filter(question_id=question_instance)
        if res.selected_option:
            option_list=ast.literal_eval(str(res.selected_option))
            if len(answer_instances)==len(option_list):
                flag=0
                for j in range(len(answer_instances)):
                    if answer_instances[j].option!=option_list[j]:
                        flag=1
                if flag==0:
                    print('yes')
                    marks=marks+res.question_id.marks
            else:
                pass
        total_marks=total_marks+res.question_id.marks
    result_instance=result(quiz_id=quiz_instance,student_id=student_instance,marks_obtained=marks,total_marks=total_marks)
    result_instance.save()
    return render(request,'quiz/quiz_result.html',{'marks':marks,'total_marks':total_marks, 'class_name': class_name})