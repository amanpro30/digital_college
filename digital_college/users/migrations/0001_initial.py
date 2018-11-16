<<<<<<< HEAD
# Generated by Django 2.1.2 on 2018-11-14 19:31
=======
# Generated by Django 2.1.2 on 2018-11-15 20:11
>>>>>>> ravish

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubEnrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Clubs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CourseEnrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Registered_College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_Of_College', models.CharField(max_length=100)),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('College_Registration_Number', models.IntegerField()),
                ('City', models.CharField(max_length=25)),
                ('State', models.CharField(max_length=25)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Registered_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('activation_key', models.CharField(max_length=255)),
                ('email_validated', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('role', models.CharField(choices=[('F', 'faculty'), ('S', 'student')], max_length=1)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('college_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='users.Registered_College')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='courses',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Registered_User'),
        ),
        migrations.AddField(
            model_name='courseenrollment',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Courses'),
        ),
        migrations.AddField(
            model_name='courseenrollment',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Registered_User'),
        ),
        migrations.AddField(
            model_name='clubs',
            name='club_head',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Registered_User'),
        ),
        migrations.AddField(
            model_name='clubs',
            name='college_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Registered_College'),
        ),
        migrations.AddField(
            model_name='clubenrollment',
            name='club_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Clubs'),
        ),
        migrations.AddField(
            model_name='clubenrollment',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Registered_User'),
        ),
    ]
