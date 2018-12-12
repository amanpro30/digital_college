from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import reverse
from quiz.models import quiz,singlechoice,multiplechoice,truefalse,answers,respo_single,respo_multiple,respo_true,result
from users.models import Registered_College,Registered_User,Courses,CourseEnrollment,Clubs,ClubEnrollment,Exam

# Create your tests here.


#Model Testing
class TestUserModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user=User.objects.create_user(username='testuser',password='testpass')
        test_user2=User.objects.create_user(username='testuser2',password='testpass2')
        Registered_College.objects.create(
            user=test_user,
            Name_Of_College='test_college',
            email='test_college@gmail.com',
            College_Registration_Number=12345,
            City='Sri City',
            State='Andhra Pradesh',
        )
        test_college=Registered_College.objects.get(id=1)
        Registered_User.objects.create(
            user=test_user,
            First_Name='test_fac',
            Last_Name='user',
            email='test_user_fac@gmail.com',
            role='F',
            college_id=test_college,
        )
        test_faculty=Registered_User.objects.get(role='F')
        Registered_User.objects.create(
            user=test_user2,
            First_Name='test_stud',
            Last_Name='user',
            email='test_user_stud@gmail.com',
            role='S',
            college_id=test_college,
        )
        test_student=Registered_User.objects.get(role='S')
        Courses.objects.create(
            course_name='test_course',
            faculty_id=test_faculty,
            college_id=test_college
        )
        test_course=Courses.objects.get(id=1)
        quiz.objects.create(
            college_id=test_college,
            class_id=test_course,
            name_of_quiz='test_quiz',
            instructions='this is just a fun exam',
            start_time='2018-12-12 12:00:00',
            end_time='2018-12-12 12:00:00',
        )
    def test_user_creation(self):
        test_user=User.objects.get(id=1)
        self.assertTrue(isinstance(test_user,User))
        self.assertEqual(test_user.username,'testuser')
    def test_single_choice_creation(self):
        test_college=Registered_College.objects.get(id=1)
        test_course=Courses.objects.get(id=1)
        test_quiz=quiz.objects.get(id=1)
        singlechoice.objects.create(
            college_id=test_college,
            class_id=test_course,
            quiz_id=test_quiz,
            question='single_ques',
            option1='single_option1',
            option2='single_option2',
            option3='single_option3',
            option4='single_option4',
            answer='A',
            marks=5
        )
        test_single=singlechoice.objects.get(id=1)
        self.assertTrue(isinstance(test_single,singlechoice))
        self.assertEqual(test_single.question,'single_ques')
        self.assertEqual(test_single.option1,'single_option1')
        self.assertEqual(test_single.marks,5)
    def test_multiple_choice_creation(self):
        test_college=Registered_College.objects.get(id=1)
        test_course=Courses.objects.get(id=1)
        test_quiz=quiz.objects.get(id=1)
        multiplechoice.objects.create(
            college_id=test_college,
            class_id=test_course,
            quiz_id=test_quiz,
            question='multiple_ques',
            option1='multiple_option1',
            option2='multiple_option2',
            option3='multiple_option3',
            option4='multiple_option4',
            marks=5
        )
        test_multiple=multiplechoice.objects.get(id=1)
        self.assertTrue(isinstance(test_multiple,multiplechoice))
        self.assertEqual(test_single.question,'multiple_ques')
        self.assertEqual(test_single.option1,'multiple_option1')
        self.assertEqual(test_single.marks,5)
    def test_true_false_creation(self):
        test_college=Registered_College.objects.get(id=1)
        test_course=Courses.objects.get(id=1)
        test_quiz=quiz.objects.get(id=1)
        truefalse.objects.create(
             college_id=test_college,
               class_id=test_course,
              quiz_id=test_quiz,
              question='true_ques',
              option1='true_option1',
              marks=5,
              answer='A'
        )
        test_true=truefalse.objects.get(id=1)
        self.assertTrue(isinstance(test_true,truefalse))
        self.assertEqual(test_true.question,'true_ques')
        self.assertEqual(test_true.option1,'true_option1')
        self.assertEqual(test_true.marks,5)
    def test_respo_single(self):
        test_user=User.objects.get(id=1)
        test_quiz=quiz.objects.get(id=1)
        test_question=singlechoice.objects.get(id=1)
        user_id=test_user
        quiz_id=test_quiz
        question_id=test_question
        respo_single.objects.create(
            user_id=test_user,
            quiz_id=test_quiz,
            question_id=test_question,
            selected_option='A'
        )
        test_response=respo_single.objects.get(id=1)
        self.assertTrue(isinstance(test_response,respo_single))
        self.assertEqual(test_true.question,'true_ques')
        self.assertEqual(test_true.option1,'true_option1')
        self.assertEqual(test_true.marks,5)           
#         test_course=Courses.objects.get(id=1)
#         self.assertTrue(isinstance(test_course,Courses))
#         self.assertEqual(test_course.course_name,'test_course')
#     def test_course_enrollment(self):
#         test_course=Courses.objects.get(id=1)
#         test_student=Registered_User.objects.get(role='S')
#         CourseEnrollment.objects.create(
#             course_id=test_course,
#             student_id=test_student
#         )
#         test_course_enrollment=CourseEnrollment.objects.get(id=1)
#         self.assertTrue(isinstance(test_course_enrollment,CourseEnrollment))
#         self.assertEqual(test_course.course_name,'test_course')


# #views testing
# class TestUserView(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.client = Client()
#         cls.user = User.objects.create_user(
#         username='testuser',
#         password='testpass'
#         )
#     def test_view_coll_reg_accessible_by_name_and_correct_template(self):
#         resp = self.client.get(reverse('users:College_Registration'))
#         self.assertEqual(resp.status_code, 200)
#         self.assertTemplateUsed(resp, 'users/College_Registration.html')
#     def test_view_user_reg_accessible_by_name_and_correct_template(self):
#         resp = self.client.get(reverse('users:User_Registration'))
#         self.assertEqual(resp.status_code, 200)
#         self.assertTemplateUsed(resp, 'users/User_Registration.html')
#     def test_view_add_course_accessible_by_name_and_correct_template(self):
#         resp = self.client.get(reverse('users:add_courses'))
#         self.assertEqual(resp.status_code, 200)
#         self.assertTemplateUsed(resp, 'users/Add_Course.html')
#     def test_view_reset_accessible_by_name_and_correct_template(self):
#         resp = self.client.get(reverse('users:reset'))
#         self.assertEqual(resp.status_code, 200)
#         self.assertTemplateUsed(resp, 'users/password_reset_form.html')