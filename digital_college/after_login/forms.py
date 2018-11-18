from django.forms import ModelForm

from users.models import Registered_User


class Profile(ModelForm):

    class Meta:
        model = Registered_User
        fields = ['First_Name', 'Last_Name', 'email', 'image', 'mobile_no']
