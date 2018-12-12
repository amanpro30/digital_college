from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import reverse
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
    def test_user_creation(self):
        test_user=User.objects.get(id=1)
        self.assertTrue(isinstance(test_user,User))
        self.assertEqual(test_user.username,'testuser')
    def test_reg_college_creation(self):
        test_college=Registered_College.objects.get(id=1)
        self.assertTrue(isinstance(test_college,Registered_College))
        self.assertEqual(test_college.Name_Of_College,'test_college')
    def test_reg_faculty_creation(self):
        test_faculty=Registered_User.objects.get(role='F')
        self.assertTrue(isinstance(test_faculty,Registered_User))
        self.assertEqual(test_faculty.First_Name,'test_fac')
    def test_course_creation(self):
        test_course=Courses.objects.get(id=1)
        self.assertTrue(isinstance(test_course,Courses))
        self.assertEqual(test_course.course_name,'test_course')
    def test_course_enrollment(self):
        test_course=Courses.objects.get(id=1)
        test_student=Registered_User.objects.get(role='S')
        CourseEnrollment.objects.create(
            course_id=test_course,
            student_id=test_student
        )
        test_course_enrollment=CourseEnrollment.objects.get(id=1)
        self.assertTrue(isinstance(test_course_enrollment,CourseEnrollment))
        self.assertEqual(test_course.course_name,'test_course')


#views testing
class TestUserView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create_user(
        username='testuser',
        password='testpass'
        )
    def test_view_coll_reg_accessible_by_name_and_correct_template(self):
        resp = self.client.get(reverse('users:College_Registration'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'users/College_Registration.html')
    def test_view_user_reg_accessible_by_name_and_correct_template(self):
        resp = self.client.get(reverse('users:User_Registration'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'users/User_Registration.html')
    def test_view_add_course_accessible_by_name_and_correct_template(self):
        resp = self.client.get(reverse('users:add_courses'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'users/Add_Course.html')
    def test_view_reset_accessible_by_name_and_correct_template(self):
        resp = self.client.get(reverse('users:reset'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'users/password_reset_form.html')