from collections import namedtuple

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from quiz.api.serializers import QuizSetSerializer
from quiz.models import multiplechoice, singlechoice, truefalse

QuizSet = namedtuple('QuizSetSerializer', ('mcq', 'scq', 'tf'))


class QuizView(APIView):

    def get(self, request, quiz_id, class_name):
        user = request.user
        try:
            if user.registered_college.id:
                quizset = QuizSet(mcq=multiplechoice.objects.filter(quiz_id=quiz_id),
                                  scq=singlechoice.objects.filter(quiz_id=quiz_id),
                                  tf=truefalse.objects.filter(quiz_id=quiz_id))
                serializer = QuizSetSerializer(quizset)
                return Response(serializer.data)
        except:
            if user.registered_user.role == 'F':
                quizset = QuizSet(mcq=multiplechoice.objects.filter(quiz_id=quiz_id),
                                  scq=singlechoice.objects.filter(quiz_id=quiz_id),
                                  tf=truefalse.objects.filter(quiz_id=quiz_id))
                serializer = QuizSetSerializer(quizset)
                return Response(serializer.data)
        return HttpResponse('Unauthorized', status=401)
