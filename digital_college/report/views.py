from django.shortcuts import render
from users.models import Exam

# Create your views here.


def test(request, class_name):
    return render(request, 'report/student_graph.html')


def test1(request):
    return render(request, 'report/faculty_graph.html')


def exam_result(request):
    file = "grade_data.csv"
    path = 'report'
    F = open(path+'\\'+file, mode='r')

    try:
        line = F.readlines()
        print(line)
        n = 0
        data = []
        for i in line:
            buffer1 = i.split("\n")
            buffer2 = buffer1[0].split("\t")
            buffer2 = buffer2[0].split(",")
            data.append(buffer2)
            n = n + 1
            size = int(len(data))

    finally:
        F.close()





