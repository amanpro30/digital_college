from rest_framework import serializers
from quiz.models import *
from django.contrib.auth.models import User


class DjangoUserSearializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registered_User
        fields = ('id',)


class CoursesSerializer(serializers.ModelSerializer):
    # faculty_id = UserSerializer()

    class Meta:
        model = Courses
        fields = ('faculty_id',)

    # def create(self, validated_data):
    #     faculty_id_data = validated_data.pop('faculty_id')
    #     faculty_id = Registered_User.objects.create(**faculty_id_data)
    #     cor = Courses.objects.create(faculty_id=faculty_id, **validated_data)
    #     return cor


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registered_College
        fields = ('Name_Of_College',)


class QuizInfoSerializer(serializers.ModelSerializer):
    class_id = CoursesSerializer()
    class_id.faculty_id = UserSerializer()
    college_id = CollegeSerializer()

    class Meta:
        model = quiz
        fields = ('name_of_quiz', 'instructions', 'start_time', 'end_time', 'class_id', 'college_id')

    def create(self, validated_data):
        class_id_data = validated_data.pop('class_id')
        class_id = Courses.objects.create(**class_id_data)
        class_faculty_id = validated_data.pop('Courses.faculty_id')
        class_id.faculty_id = Registered_User.objects.create(**class_faculty_id)
        college_id_data = validated_data.pop('college_id')
        college_id = Registered_College.objects.create(**college_id_data)
        quz = quiz.objects.create(college_id=college_id, class_id=class_id, **validated_data)
        return quz


class MultipleChoiceSerializer(serializers.ModelSerializer):
    quiz_info = QuizInfoSerializer()

    class Meta:
        model = multiplechoice
        fields = ('quiz_id', 'question', 'option1', 'option2', 'option3', 'option4', 'marks')

    def create(self, validated_data):
        quiz_id_data = validated_data.pop('quiz_id')
        quiz_id = quiz.objects.create(**quiz_id_data)
        mcq = multiplechoice.objects.create(quiz_id=quiz_id, **validated_data)
        return mcq


class MultipleChoiceAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = answers
        fields = ('question_id', 'option')


class SingleChoiceSerializer(serializers.ModelSerializer):
    quiz_info = QuizInfoSerializer()

    class Meta:
        model = singlechoice
        fields = ('quiz_id', 'question', 'option1', 'option2', 'option3', 'option4', 'marks', 'answer')

        def create(self, validated_data):
            quiz_id_data = validated_data.pop('quiz_id')
            quiz_id = quiz.objects.create(**quiz_id_data)
            scq = singlechoice.objects.create(quiz_id=quiz_id, **validated_data)
            return scq


class TrueFalseSerializer(serializers.ModelSerializer):
    quiz_info = QuizInfoSerializer()

    class Meta:
        model = truefalse
        fields = ('quiz_id', 'question', 'option1', 'marks', 'answer')

    def create(self, validated_data):
        quiz_id_data = validated_data.pop('quiz_id')
        quiz_id = quiz.objects.create(**quiz_id_data)
        tf = truefalse.objects.create(quiz_id=quiz_id, **validated_data)
        return tf
