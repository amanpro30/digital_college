from django.shortcuts import redirect
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from quiz.models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
import io
from rest_framework.parsers import JSONParser


class QuizView(APIView):

    def get(self, request, class_name):
        user = request.user
        course = Courses.objects.get(course_name=class_name, college_id=user.registered_user.college_id)
        quiz_info = quiz.objects.filter(class_id=course, college_id=user.registered_user.college_id)
        serializer = QuizInfoSerializer(quiz_info, many=True)
        return Response(serializer.data)

    def post(self, request, class_name):
        user = request.user
        serializer = QuizInfoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


# if user.registered_user.role == 'F':
# deserializer
# json = JSONRenderer().render(serializer.validated_data)
# stream = io.BytesIO(json)
# data = JSONParser().parse(stream)
# print(data['name_of_quiz'])

class MultipleChoiceView(APIView):

    def get(self, request, class_name, quiz_id):
        user = request.user
        course = Courses.objects.get(course_name=class_name, college_id=user.registered_user.college_id)
        quiz_info = quiz.objects.filter(class_id=course, college_id=user.registered_user.college_id)

        serializer = QuizInfoSerializer(quiz_info, many=True)
        return Response(serializer.data)

    def post(self, request, class_name):
        user = request.user
        serializer = QuizInfoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            if user.registered_user.role == 'F':
                # deserializer
                json = JSONRenderer().render(serializer.data)
                stream = io.BytesIO(json)
                data = JSONParser().parse(stream)
                print(data['name_of_quiz'])
                a = quiz(college_id=user.registered_user.college_id,
                         class_id=Courses.objects.get(course_name=class_name,
                                                      college_id=user.registered_user.college_id),
                         name_of_quiz=data['name_of_quiz'], instructions=data['instructions'],
                         start_time=data['start_time'], end_time=data['end_time']
                         )
                a.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
