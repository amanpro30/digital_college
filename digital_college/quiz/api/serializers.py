from collections import namedtuple

from rest_framework import serializers
from quiz.models import *


class MultipleChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = multiplechoice
        fields = ('question', 'option1', 'option2', 'option3', 'option4', 'marks')


class MultipleChoiceAnswerSerializer(serializers.ModelSerializer):
    mcq = MultipleChoiceSerializer()

    class Meta:
        model = answers
        fields = ('question_id', 'option')

    def create(self, validated_data):
        mcq_id_data = validated_data.pop('question_id')
        mcqid = multiplechoice.objects.create(**mcq_id_data)
        mcqa = answers.objects.create(question_id=mcqid, **validated_data)
        return mcqa


class SingleChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = singlechoice
        fields = ('question', 'option1', 'option2', 'option3', 'option4', 'marks', 'answer')


class TrueFalseSerializer(serializers.ModelSerializer):
    class Meta:
        model = truefalse
        fields = ('question', 'option1', 'marks', 'answer')


class QuizSetSerializer(serializers.Serializer):
    mcq = MultipleChoiceSerializer(many=True)
    scq = SingleChoiceSerializer(many=True)
    tf = TrueFalseSerializer(many=True)


